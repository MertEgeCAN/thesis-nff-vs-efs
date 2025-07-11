import config
from source.a_generate.c_test import Test


class Suite:
    def __init__(self):
        self.tests = self.generate_tests()

    def generate_tests(self):
        tests = []
        for i in range(config.MAX_TEST):
            tests.append(Test(i + 1))
        return tests
