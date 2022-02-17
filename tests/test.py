from xunit.testcase import TestCase
from xunit.wasrun import WasRun

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testmethod")

    def test_running(self):
        self.test.run()
        assert self.test.wasRun

    def test_setup(self):
        self.test.run()
        assert self.test.log == "setUp testmethod "

    def test_template_method(self):
        test = WasRun("testmethod")
        test.run()
        assert test.log == "setUp testmethod "

if __name__ == "__main__":
    TestCaseTest("test_running").run()
    TestCaseTest("test_setup").run()
