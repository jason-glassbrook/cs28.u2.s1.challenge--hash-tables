import unittest

from .ex1 import get_indices_of_item_weights


class TestEx1(unittest.TestCase):

    def test_ex1_1(self):
        weights = [9]
        result = get_indices_of_item_weights(weights, 1, 9)
        self.assertIs(None, result)

    def test_ex1_2(self):
        weights = [4, 4]
        result = get_indices_of_item_weights(weights, 2, 8)
        self.assertCountEqual((0, 1), result)

    def test_ex1_3(self):
        weights = [4, 6, 10, 15, 16]
        result = get_indices_of_item_weights(weights, 5, 21)
        self.assertCountEqual((1, 3), result)

    def test_ex1_4(self):
        weights = [12, 6, 7, 14, 19, 3, 0, 25, 40]
        result = get_indices_of_item_weights(weights, 9, 7)
        self.assertCountEqual((2, 6), result)


if __name__ == "__main__":
    unittest.main()
