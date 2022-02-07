from xunit.testcase import TestCase

class WasRun(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.wasRun = None

    def testmethod(self):
        self.wasRun = 1

