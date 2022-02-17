from xunit.testcase import TestCase

class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)

    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1

    def testmethod(self):
        self.wasRun = 1

