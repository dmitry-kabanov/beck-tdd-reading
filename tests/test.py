from xunit.testcase import TestCase
from xunit.wasrun import WasRun
from xunit.testresult import TestResult
from xunit.testsuite import TestSuite


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testmethod")

    def test_running(self):
        result = TestResult()
        self.test.run(result)
        assert self.test.wasRun

    def test_template_method(self):
        test = WasRun("testmethod")
        result = TestResult()
        test.run(result)
        assert test.log == "setUp testmethod tearDown "

    def test_result(self):
        test = WasRun("testmethod")
        result = TestResult()
        test.run(result)
        assert(result.summary() == "1 run, 0 failed")

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        result = TestResult()
        test.run(result)
        assert(result.summary() == "1 run, 1 failed")

    def test_failed_result_formatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert(result.summary() == "1 run, 1 failed")

    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_broken_method"))
        result = TestResult()
        suite.run(result)
        assert(result.summary() == "2 run, 1 failed")


if __name__ == "__main__":
    suite = TestSuite()
    suite.add(TestCaseTest("test_running"))
    suite.add(TestCaseTest("test_template_method"))
    suite.add(TestCaseTest("test_result"))
    suite.add(TestCaseTest("test_failed_result"))
    suite.add(TestCaseTest("test_failed_result_formatting"))
    result = TestResult()
    suite.run(result)
    print(result.summary())
