from xunit.testcase import TestCase


class TestCaseWithBrokenSetup(TestCase):
    def setUp(self):
        raise Exception

    def test_method(self):
        pass
