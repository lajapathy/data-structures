
import unittest

class SimplisticTest(unittest.TestCase):
    def test_pass(self):
        self.assertTrue(True)

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError('Test error!')

    def test_assert(self):
        try:
            assert False,"testing"
        except Exception:
            print("sss")


if __name__ == '__main__':
    s=SimplisticTest()
    s.test_assert()