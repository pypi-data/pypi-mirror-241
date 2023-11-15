""" CLI for code pipeline """
import argparse

import boto3

from codepiper.debug import run_debug
from codepiper.pipeline_clear import verify_clear
from codepiper.rollback import rollback_pipeline
from codepiper.watch import watch_pipeline


def process_args():
    """Process CLI args."""
    parser = argparse.ArgumentParser(
        description="Manage AWS CodePipeline",
    )
    parser.add_argument(
        "--profile",
        help="Name of the AWS profile to use",
    )
    parser.add_argument(
        "--region",
        help="Name of the AWS region to use",
    )
    subparsers = parser.add_subparsers()

    watch = subparsers.add_parser("watch", help="watch pipeline activity")
    watch.set_defaults(func=watch_pipeline)
    watch.add_argument(
        "-p",
        "--pipeline",
        help="Name of the pipeline to watch",
        required=True,
    )
    watch.add_argument(
        "-e",
        "--execution-id",
        help="Id of the pipeline to watch",
    )
    watch.add_argument(
        "-f",
        "--follow-logs",
        help="Follow build logs",
        action="store_true",
    )

    debug = subparsers.add_parser("debug", help="Run stage with debug mode enabled")
    debug.set_defaults(func=run_debug)
    debug.add_argument(
        "-p",
        "--pipeline",
        help="Name of the pipeline containing the stage to debug",
        required=True,
    )
    debug.add_argument(
        "-s",
        "--stage",
        help="Name of the stage to run in debug mode",
        required=True,
    )
    debug.add_argument(
        "-e",
        "--envvar",
        metavar="VAR_NAME=VALUE",
        help="Add or override an env var in debug mode. If a value "
             "contains spaces, define it using double quotes. Ex: "
             'JAVA_OPTS="-Xmx1g -Dproperty=value"',
        nargs="+",
        required=False,
    )
    debug.add_argument(
        "-d",
        "--dryrun",
        help="Dryrun mode",
        action="store_true",
    )

    verifier = subparsers.add_parser("verify_clear", help="verify pipeline is clear")
    verifier.set_defaults(func=verify_clear)
    verifier.add_argument(
        "-p",
        "--pipeline",
        help="Name of the pipeline to verify clear",
        required=True,
    )

    rollback = subparsers.add_parser(
        "rollback", help="rollback pipeline stage to prior state"
    )
    rollback.add_argument(
        "-d",
        "--dryrun",
        help="Dryrun mode",
        action="store_true",
    )
    rollback.add_argument(
        "-p",
        "--pipeline",
        help="Name of the pipeline to rollback",
        required=True,
    )
    rollback.add_argument(
        "-s",
        "--stage",
        help="Name of the pipeline stage to rollback",
        required=True,
    )
    rollback.add_argument(
        "-c",
        "--commit",
        help="Commit to rollback to (default: last successful commit for stage)",
    )
    rollback.add_argument(
        "-n",
        "--no-wait",
        action="store_true",
        help="Don't wait for the rollback - run in background",
    )
    rollback.add_argument(
        "-f",
        "--follow-logs",
        help="Follow build logs",
        action="store_true",
    )
    rollback.set_defaults(func=rollback_pipeline)
    args = vars(parser.parse_args())
    if "func" in args:
        args["func"](
            session=boto3.session.Session(
                profile_name=args["profile"], region_name=args["region"]
            ),
            **args
        )
    else:
        parser.print_help()


def main():
    """Main entrypoint."""
    process_args()


if __name__ == "__main__":
    main()
