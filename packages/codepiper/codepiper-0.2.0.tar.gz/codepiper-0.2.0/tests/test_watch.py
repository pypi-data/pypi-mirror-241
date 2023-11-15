import os
import unittest
import boto3
import time
from .zpill import PillTest
from codepiper.watch import PipelineState


class TestPipelineState(PillTest):
    def test_get_activity(self):
        session = self.pill_session("test_get_activity")
        pipeline_state = PipelineState(
            session=session,
            pipeline_name="sample",
        )

        activities, keep_watching = pipeline_state.get_activity()

        assert keep_watching == True
        assert len(activities) == 1
        assert len(activities[0].execution.execution_id) > 0
        assert len(activities[0].execution.commit_id) > 0
        assert len(activities[0].execution.commit_message) > 0
        assert "Succeeded" == activities[0].status
        assert "deploy" == activities[0].action
        assert "Succeeded" == activities[0].status
        assert activities[0].last_status_change
        assert None == activities[0].error_message
        assert (
            "sample-deploy:657fd506-b171-4296-b2dd-926d066466ed"
            == activities[0].codebuild_id
        )
