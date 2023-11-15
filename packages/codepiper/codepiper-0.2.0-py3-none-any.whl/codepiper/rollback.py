""" Rollback pipeline """

import json
from typing import Optional

from boto3.session import Session

from codepiper.build import BuildMonitor
from codepiper.context import LogContextManager
from codepiper.utils import get_build_args, run_build, get_latest_execution_id, action_last_update_time


def rollback_pipeline(
    session: Session,
    pipeline: str,
    stage: str,
    commit: Optional[str] = None,
    dryrun: bool = False,
    no_wait: bool = False,
    follow_logs: bool = False,
    **kwargs,
):
    """Rollback a pipeline to a prior execution"""
    execution_id = get_latest_execution_id(
        session=session,
        pipeline=pipeline,
        stage=stage,
        commit=commit,
    )

    print(f"Rollback to {execution_id}")

    codepipeline = session.client("codepipeline")

    # find source info
    commit_id = "???"
    commit_message = ""
    artifacts = codepipeline.get_pipeline_execution(
        pipelineName=pipeline,
        pipelineExecutionId=execution_id,
    )["pipelineExecution"]["artifactRevisions"]
    for artifact in artifacts:
        if "revisionSummary" in artifact:
            try:
                revision_summary = json.loads(artifact["revisionSummary"])
                if revision_summary["ProviderType"] == "GitHub":
                    commit_id = artifact["revisionId"]
                    commit_message = revision_summary["CommitMessage"]
            except:
                commit_id = artifact["revisionId"]
                commit_message = artifact["revisionSummary"]

    actions = codepipeline.list_action_executions(
        pipelineName=pipeline, filter={"pipelineExecutionId": execution_id}
    )

    ctx_mgr = LogContextManager()
    builds = BuildMonitor(session=session)

    details = actions["actionExecutionDetails"]
    details.sort(key=action_last_update_time)

    for action in details:
        if action["stageName"] != stage:
            continue

        if action["input"]["actionTypeId"]["provider"] == "CodeBuild":
            if len(action["output"]["outputArtifacts"]) > 0:
                primary_artifact = action["output"]["outputArtifacts"][0]
            else:
                primary_artifact = None

            if "executionResult" in action["output"]:

                build_kwargs = get_build_args(
                    session=session,
                    build_id=action["output"]["executionResult"]["externalExecutionId"],
                    output_artifact=primary_artifact,
                )

                build = run_build(
                    session=session,
                    build_kwargs=build_kwargs,
                    dryrun=dryrun,
                )

                if not dryrun and not no_wait:
                    logger = ctx_mgr.set_context(
                        build["id"],
                        commit_id=commit_id,
                        commit_message=commit_message,
                        status="Rollback ▶",
                    )

                    build_future = builds.monitor(
                        build["id"],
                        follow_logs=follow_logs,
                        logger=logger,
                    )
                    build_future.result()
                    ctx_mgr.clear_context(build["id"])
