from codepiper.debug import run_debug

from .zpill import PillTest


class TestDebugging(PillTest):
    def test_debug_stage(self):
        session = self.pill_session("test_debug_stage")
        run_debug(
            session=session,
            pipeline="sample",
            stage="Staging",
            envvar=["VARONE=test", 'VARTWO="test two"'],
        )

    def test_debug_stage_dryrun(self):
        session = self.pill_session("test_debug_stage")
        run_debug(
            session=session,
            pipeline="sample",
            stage="Staging",
            envvar=["VARONE=test", 'VARTWO="test two"'],
            dryrun=True,
        )
