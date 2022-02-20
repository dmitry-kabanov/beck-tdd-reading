from xunit.testresult import TestResult

class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self, result: TestResult):
        result.testStarted()
        try:
            self.setUp()
        except:
            result.setUpErrored()
            return result
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
        return result

    def tearDown(self):
        pass
