import unittest

from main.main import addNumbers


class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        return

    def testAddNumbers(self):
        x = 3
        y = 5
        expected_result = 8
        actual_result = addNumbers(x=x, y=y)
        self.assertEqual(first=expected_result, second=actual_result)


if __name__ == '__main__':
    unittest.main()
