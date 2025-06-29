from . import config
from source.generate_2.test import Test


class Suite:
    def __init__(self):
        self.tests = self.generate_tests()

    def generate_tests(self):
        tests = []
        for i in range(config.MAX_TEST):
            tests.append(Test(i))
        return tests
