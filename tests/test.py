from xunit.testcase import TestCase
from xunit.wasrun import WasRun

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testmethod")

    def test_running(self):
        self.test.run()
        assert self.test.wasRun

    def test_template_method(self):
        test = WasRun("testmethod")
        test.run()
        assert test.log == "setUp testmethod tearDown "

    def test_result(self):
        test = WasRun("testmethod")
        result = test.run()
        assert(result.summary() == "1 run, 0 failed")

if __name__ == "__main__":
    TestCaseTest("test_running").run()
    TestCaseTest("test_template_method").run()
    TestCaseTest("test_result").run()
