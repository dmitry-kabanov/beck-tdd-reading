from xunit.testcase import TestCase
from xunit.wasrun import WasRun

class TestCaseTest(TestCase):
    def test_running(self):
        test = WasRun("testmethod")
        test.run()
        assert test.wasRun

    def test_setup(self):
        test = WasRun("testmethod")
        test.run()
        assert test.wasSetUp

if __name__ == "__main__":
    TestCaseTest("test_running").run()
    TestCaseTest("test_setup").run()
