class WasRun:
    def __init__(self, name):
        self.name = name
        self.wasRun = None

    def testmethod(self):
        self.wasRun = 1

    def run(self):
        method = getattr(self, self.name)
        method()
