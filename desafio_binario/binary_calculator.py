class BinaryCalculator:

    def __init__(self, value):
        self.value = int(value, 2)
        self.result = 0

    @staticmethod
    def _verbose(value):
        size = 8 - len(value) + 2 if len(value) < 8 else None
        if size:
            convert = value.replace('0b', '0' * size)
            return convert

    def __add__(self, other):
        sum = bin(self.value + other.value)
        return self._verbose(sum)

    def __sub__(self, other):
        sub = bin(self.value - other.value)
        return self._verbose(sub)

    def __mul__(self, other):
        mul = bin(self.value * other.value)
        return self._verbose(mul)


    def __mod__(self, other):
        mod = bin(self.value % other.value)
        return self._verbose(mod)


    def __repr__(self):
        return f'BinaryCalculator({bin(self.value)[2:]})'
