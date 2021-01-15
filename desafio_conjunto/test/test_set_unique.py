import unittest

from desafio_conjunto.return_unique import unique_with_set, unique_with_for


class TestUniqueSet(unittest.TestCase):

    def test_if_values_are_unique_with_for(self):
        self.assertTrue(unique_with_for(5) != unique_with_for(5))

    def test_if_values_are_unique_with_set(self):
        self.assertTrue(unique_with_set(5) != unique_with_set(5))


if __name__ == '__main__':
    unittest.main()
