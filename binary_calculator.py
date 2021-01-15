from bitstring import BitArray


class BinaryCalculator:



    def __init__(self, num1: str, num2: str):
        self.num1 = BitArray(bin=num1)
        self.num2 = BitArray(bin=num2)

    def sum_binary(self, verbose=False):
        num1 = self.num1.int
        num2 = self.num2.int
        result = bin(num1 + num2)
        if verbose:
            size = 8 - len(result)
            if size > 0:
                return result.replace('0b', '0' * (size + 2))
        return result

    def sub_binary(self, verbose=False):
        num1 = self.num1.int
        num2 = self.num2.int
        result = bin(num1 - num2)
        if verbose:
            size = 8 - len(result)
            if size > 0:
                return result.replace('0b', '0' * (size + 2))
        return result

    def mul_binary(self, verbose: bool = False):
        num1 = self.num1.int
        num2 = self.num2.int
        result = bin(num1 * num2)
        if verbose:
            size = 8 - len(result)
            if size > 0:
                return result.replace('0b', '0' * (size + 2))
        return result

    def div_binary(self, verbose: bool = False):
        num1 = self.num1.int
        num2 = self.num2.int
        to_int = (int(num1 / num2))
        result = bin(to_int)
        if verbose:
            size = 8 - len(result)
            if size > 0:
                return result.replace('0b', '0' * (size + 2))
        return result

    def mod_binary(self, verbose: bool = False):
        num1 = self.num1.int
        num2 = self.num2.int
        result = bin(num1 % num2)
        if verbose:
            size = 8 - len(result)
            if size > 0:
                return result.replace('0b', '0' * (size + 2))
        return result
