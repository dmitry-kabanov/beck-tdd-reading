from xunit.testcase import TestCase
from xunit.wasrun import WasRun

class TestCaseTest(TestCase):
    def test_running(self):
        test = WasRun("testmethod")
        assert not test.wasRun
        test.run()
        assert test.wasRun

if __name__ == "__main__":
    TestCaseTest("test_running").run()
