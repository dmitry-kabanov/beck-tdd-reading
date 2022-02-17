from xunit.testcase import TestCase

class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1
        self.log = "setUp "

    def testmethod(self):
        self.wasRun = 1
        self.log += "testmethod "

    def tearDown(self):
        self.log += "tearDown "

