""" Run a pipeline stage in debug mode."""
from typing import Optional

from boto3.session import Session

from codepiper.utils import (action_last_update_time, get_build_args,
                             get_latest_execution_id, parse_key_val, run_build)


def run_debug(
    session: Session,
    pipeline: str,
    stage: str,
    envvar: Optional[str] = None,
    dryrun: bool = False,
    **kwargs,
):
    del kwargs

    exec_id = get_latest_execution_id(
        session=session,
        pipeline=pipeline,
        stage=stage,
        any_status=True,
    )
    print(f"🐛 Debugging {exec_id}")

    codepipeline = session.client("codepipeline")

    actions = codepipeline.list_action_executions(
        pipelineName=pipeline, filter={"pipelineExecutionId": exec_id}
    )
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
                    env_vars=parse_key_val(envvar),
                    debug_session=True,
                )

                print("♻️  Starting build...")
                build = run_build(
                    session=session,
                    build_kwargs=build_kwargs,
                    dryrun=dryrun,
                )

                if not dryrun:
                    project_id = build["id"].split(":")
                    account_id = session.client("sts").get_caller_identity()["Account"]
                    print(
                        "🔗 Follow the build URL and use the AWS Session Manager link to enter the build container: "
                        f"https://{session.region_name}.console.aws.amazon.com/codesuite/codebuild/{account_id}/projects/{project_id[0]}/build/{project_id[0]}%3A{project_id[1]}?region={session.region_name}"
                    )
