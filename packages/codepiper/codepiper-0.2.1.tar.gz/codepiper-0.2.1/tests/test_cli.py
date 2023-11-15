import sys
import unittest
from mock import patch
from codepiper import cli


class TestCli(unittest.TestCase):
    """Test cases for cli."""

    def test_usage(self):
        """Test the cli usage printout."""
        args = ["cli", "--help"]
        with patch.object(sys, "argv", args):
            with self.assertRaises(SystemExit):
                cli.main()
