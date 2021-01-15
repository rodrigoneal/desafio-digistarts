class BinaryCalculator:

    def __init__(self, value):
        self.value = int(value, 2)

    def __add__(self, other):
        result = bin(self.value + other.value)
        size = 8 - len(result) + 2 if len(result) < 8 else None
        if size:
            result = result.replace('0b', '0' * size)
        return result

    def __sub__(self, other):
        result = bin(self.value - other.value)
        size = 8 - len(result) + 2 if len(result) < 8 else None
        if size:
            result = result.replace('0b', '0' * size)
        return result

    def __mul__(self, other):
        result = bin(self.value * other.value)
        size = 8 - len(result) + 2 if len(result) < 8 else None
        if size:
            result = result.replace('0b', '0' * size)
        return result

    def __mod__(self, other):
        result = bin(self.value % other.value)
        size = 8 - len(result) + 2 if len(result) < 8 else None
        if size:
            result = result.replace('0b', '0' * size)
        return result

    def __repr__(self):
        return f'BinaryCalculator({bin(self.value)[2:0]})'



