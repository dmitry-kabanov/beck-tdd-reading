class TestResult:
    def __init__(self):
        self.runCount = 0
        self.fails = 0
        self.errors = 0

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.fails += 1

    def setUpErrored(self):
        self.errors += 1

    def summary(self):
        message = "%d run, %d failed" % (self.runCount, self.fails)

        if self.errors:
            message += ", %d errored" % self.errors

        return message
