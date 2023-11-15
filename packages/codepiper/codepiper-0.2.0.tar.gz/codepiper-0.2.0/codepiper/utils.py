"""Shared helper functions"""

import json
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from boto3.session import Session


def run_build(
    session: Session,
    build_kwargs: Dict[str, Any],
    dryrun: bool = True,
):
    """Run a build"""
    if dryrun:
        print(
            f"[DRYRUN] Would start build with args: {json.dumps(build_kwargs, indent=1)}"
        )
        return {"id": "0"}

    codebuild = session.client("codebuild")
    res = codebuild.start_build(**build_kwargs)
    return res["build"]


def parse_key_val(items: List[str]) -> Optional[Dict[str, str]]:
    """Parse a series of key-value pairs and return a dictionary."""

    def parse_var(key_val_str: str):
        var_items = key_val_str.split("=")
        key = var_items[0].strip()
        if len(var_items) > 1:
            value = "=".join(var_items[1:])
        return (key, value)

    if items:
        key_val_dict = {}
        for item in items:
            key, value = parse_var(item)
            key_val_dict[key] = value
        return key_val_dict
    return None


def get_build_args(
    session: Session,
    build_id: str,
    output_artifact: Optional[Dict[str, str]] = None,
    env_vars: Optional[Dict[str, str]] = None,
    debug_session: bool = False,
):
    """Get args from a prior build."""
    codebuild = session.client("codebuild")
    build = codebuild.batch_get_builds(ids=[build_id])["builds"][0]
    build_kwargs = {}

    def set_build_arg(dst_path, *src_path):
        val = build
        for path_part in src_path:
            if val:
                val = val.get(path_part)
        if val:
            build_kwargs[dst_path] = val

    set_build_arg("projectName", "projectName")
    set_build_arg("secondaryArtifactsOverride", "secondaryArtifacts")
    set_build_arg("environmentVariablesOverride", "environment", "environmentVariables")
    set_build_arg("sourceVersion", "sourceVersion")
    set_build_arg("sourceAuthOverride", "source", "auth")
    set_build_arg("secondarySourcesOverride", "secondarySources")
    set_build_arg("secondarySourcesVersionOverride", "secondarySourceVersions")
    set_build_arg("gitCloneDepthOverride", "source", "gitCloneDepth")
    set_build_arg("gitSubmodulesConfigOverride", "source", "gitSubmodulesConfig")
    set_build_arg("buildspecOverride", "source", "buildspec")
    set_build_arg("insecureSslOverride", "source", "insecureSsl")
    set_build_arg("buildStatusConfigOverride", "source", "buildStatusConfig")
    set_build_arg("environmentTypeOverride", "environment", "type")
    set_build_arg("imageOverride", "environment", "image")
    set_build_arg("computeTypeOverride", "environment", "computeType")
    set_build_arg("certificateOverride", "environment", "certificate")
    set_build_arg("cacheOverride", "cache")
    set_build_arg("serviceRoleOverride", "serviceRole")
    set_build_arg("privilegedModeOverride", "environment", "priviledgedMode")
    set_build_arg("timeoutInMinutesOverride", "timeoutInMinutes")
    set_build_arg("queuedTimeoutInMinutesOverride", "queuedTimeoutInMinutes")
    set_build_arg("encryptionKeyOverride", "encryptionKey")
    set_build_arg("registryCredentialOverride", "environment", "registryCredential")
    set_build_arg(
        "imagePullCredentialsTypeOverride", "environment", "imagePullCredentialsType"
    )
    set_build_arg("debugSessionEnabled", "debugSession", "sessionEnabled")
    build_kwargs["logsConfigOverride"] = {
        k: v for k, v in build["logs"].items() if k in ("cloudWatchLogs", "s3Logs")
    }
    if len(build_kwargs["logsConfigOverride"]) == 0:
        del build_kwargs["logsConfigOverride"]

    if not output_artifact:
        build_kwargs["artifactsOverride"] = {"type": "NO_ARTIFACTS"}
    elif "s3location" in output_artifact:
        build_kwargs["artifactsOverride"] = {
            "type": "S3",
            "location": output_artifact["s3location"]["bucket"],
            "path": output_artifact["s3location"]["key"],
        }
    if env_vars:
        for var_name, var_val in env_vars.items():
            cb_env_var = {
                "name": var_name,
                "value": var_val,
                "type": "PLAINTEXT",
            }
            found = False
            for idx, var_override in enumerate(
                build_kwargs["environmentVariablesOverride"]
            ):
                if var_override["name"] == var_name:
                    build_kwargs["environmentVariablesOverride"][idx] = cb_env_var
                    found = True
                    break
            if not found:
                build_kwargs["environmentVariablesOverride"].append(cb_env_var)
    build_kwargs["debugSessionEnabled"] = debug_session

    return build_kwargs


def action_last_update_time(action):
    """Used to sort by last update time."""
    return action["lastUpdateTime"]


def get_latest_execution_id(
    session: Session,
    pipeline: str,
    stage: str,
    commit: Optional[str] = None,
    any_status: bool = False,
):
    """Get the latest execution id for a pipeline."""
    codepipeline = session.client("codepipeline")
    paginator = codepipeline.get_paginator("list_action_executions")
    response_iterator = paginator.paginate(
        pipelineName=pipeline,
        filter={},
    )
    executions = {}
    for response in response_iterator:
        for action in response["actionExecutionDetails"]:
            execution_id = action["pipelineExecutionId"]
            if execution_id not in executions:
                executions[execution_id] = {
                    "last_update_time": datetime.fromtimestamp(0, timezone.utc),
                    "failed_count": 0,
                    "in_progress_count": 0,
                    "succeeded_count": 0,
                }

            if action["input"]["actionTypeId"]["category"] == "Source":
                executions[execution_id]["commit_id"] = action["output"][
                    "outputVariables"
                ].get("CommitId", "")

            if action["stageName"] != stage:
                continue

            if action["status"] == "Failed":
                executions[execution_id]["failed_count"] += 1
            if action["status"] == "InProgress":
                executions[execution_id]["in_progress_count"] += 1
            if action["status"] == "Succeeded":
                executions[execution_id]["succeeded_count"] += 1

            executions[execution_id]["last_update_time"] = max(
                executions[execution_id]["last_update_time"], action["lastUpdateTime"]
            )

    executions = [
        {
            "id": e_id,
            "lastUpdateTime": e["last_update_time"],
        }
        for e_id, e in executions.items()
        if (commit and "commit_id" in e and commit in e["commit_id"])
        or (  # only include if succeeded
            not commit
            and e["failed_count"] == 0
            and e["in_progress_count"] == 0
            and e["succeeded_count"] > 0
        )
        or (not commit and any_status)  # disregard the statuses and include
    ]
    executions.sort(key=action_last_update_time)
    if not executions:
        raise ValueError("Unable to find latest execution id")
    return executions[-1]["id"]
