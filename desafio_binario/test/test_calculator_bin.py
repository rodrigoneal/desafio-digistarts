import unittest
from desafio_binario.binary_calculator import BinaryCalculator


class TestBinaryCalculator(unittest.TestCase):

    def test_sum_return_bin_abre(self):
        self.assertEqual(BinaryCalculator('00000001', '00000011').sum_binary(), '0b100')

    def test_sum_verbose_return_bin_complete(self):
        self.assertEqual(BinaryCalculator('00000001', '00000011').sum_binary(verbose=True), '00000100')

    def test_sub_return_abre(self):
        self.assertEqual(BinaryCalculator('00000010', '00000001').sub_binary(), '0b1')

    def test_sub_verbose_return_bin_complete(self):
        self.assertEqual(BinaryCalculator('00000010', '00000001').sub_binary(verbose=True), '00000001')

    def test_mul_return_abre(self):
        self.assertEqual(BinaryCalculator('00000010', '00000001').mul_binary(), '00000001')


if __name__ == "__main__":
    unittest.main()
