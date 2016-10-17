import testtools


class NoDBTestCase(testtools.TestCase):
    USES_DB = False
