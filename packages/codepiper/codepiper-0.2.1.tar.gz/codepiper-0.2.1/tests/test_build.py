import os
import unittest
import boto3
import placebo
import time
from .zpill import PillTest
from codepiper.build import BuildMonitor
from codepiper.context import LogContext


class MockLogContext(LogContext):
    def __init__(self, ctx_id):
        self.header_messages = []
        self.write_messages = []

    def header(self, msg, *args):
        self.header_messages.append(str(msg).format(*args))

    def write(self, msg, *args):
        self.write_messages.append(str(msg).format(*args))


class TestBuildMonitor(PillTest):
    def setUp(self):
        self.logger = MockLogContext(ctx_id="test")

    def test_monitor(self):
        session = self.pill_session("test_monitor")
        monitor = BuildMonitor(session)
        monitor.monitor(
            codebuild_id="sample-build:2434a79f-ee30-4784-afd2-f0c49c0c64f0",
            follow_logs=True,
            logger=self.logger,
        )

        monitor.stop()

        time.sleep(1)

        assert len(self.logger.header_messages) == 1
        assert "phase=COMPLETED status=SUCCEEDED" in self.logger.header_messages[0]
        assert len(self.logger.write_messages) == 25
