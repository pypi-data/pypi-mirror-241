import os
import unittest
import boto3
from .zpill import PillTest
from codepiper.rollback import rollback_pipeline


class TestRollback(PillTest):
    def test_rollback_pipeline(self):
        session = self.pill_session("test_rollback_pipeline")
        pipeline_state = rollback_pipeline(
            session=session,
            pipeline="sample",
            stage="Deploy",
            dryrun=True,
        )
