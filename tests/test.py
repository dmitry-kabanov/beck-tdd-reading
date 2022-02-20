from xunit.testcase import TestCase
from xunit.wasrun import WasRun
from xunit.testresult import TestResult
from xunit.testsuite import TestSuite
from xunit.testcasewithbrokensetup import TestCaseWithBrokenSetup


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testmethod")
        self.result = TestResult()

    def test_running(self):
        self.test.run(self.result)
        assert self.test.wasRun

    def test_template_method(self):
        test = WasRun("testmethod")
        test.run(self.result)
        assert test.log == "setUp testmethod tearDown "

    def test_result(self):
        test = WasRun("testmethod")
        test.run(self.result)
        assert(self.result.summary() == "1 run, 0 failed")

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        test.run(self.result)
        assert(self.result.summary() == "1 run, 1 failed")

    def test_failed_result_formatting(self):
        self.result.testStarted()
        self.result.testFailed()
        assert(self.result.summary() == "1 run, 1 failed")

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_broken_method"))
        result = TestResult()
        suite.run(result)
        assert(result.summary() == "2 run, 1 failed")

    def test_setup_fails(self):
        self.result.testStarted()
        self.result.setUpErrored()
        assert(self.result.summary() == "1 run, 0 failed, 1 errored")

    def test_setup_fails_real_impl(self):
        test = TestCaseWithBrokenSetup("test_method")
        test.run(self.result)
        assert(self.result.summary() == "1 run, 0 failed, 1 errored")


if __name__ == "__main__":
    suite = TestSuite()
    suite.add(TestCaseTest("test_running"))
    suite.add(TestCaseTest("test_template_method"))
    suite.add(TestCaseTest("test_result"))
    suite.add(TestCaseTest("test_failed_result"))
    suite.add(TestCaseTest("test_failed_result_formatting"))
    suite.add(TestCaseTest("test_setup_fails"))
    suite.add(TestCaseTest("test_setup_fails_real_impl"))
    result = TestResult()
    suite.run(result)
    print(result.summary())
