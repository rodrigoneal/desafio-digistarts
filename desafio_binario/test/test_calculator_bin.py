import unittest
from desafio_binario.binary_calculator import BinaryCalculator


class TestBinaryCalculator(unittest.TestCase):

    def test_sum_binary_calculator(self):
        self.assertEqual(BinaryCalculator('00000001') + BinaryCalculator('00000011'), '00000100')

    def test_sub_binary_calculator(self):
        self.assertEqual(BinaryCalculator('00000010') - BinaryCalculator('00000001'), '00000001')

    def test_mul_binary_calculator(self):
        self.assertEqual(BinaryCalculator('00000001') * BinaryCalculator('00000011'), '00000011')

    def test_mod_binary_calculator(self):
        self.assertEqual(BinaryCalculator('00010100') % BinaryCalculator('00000011'), '00000010')


if __name__ == "__main__":
    unittest.main()
