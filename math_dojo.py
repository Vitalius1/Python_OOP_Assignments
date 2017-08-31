# PART 1  Support only for integerspy
class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *num_a):
        self.add_result = 0
        for value in num_a:
            self.add_result += value
        self.result += self.add_result
        return self
    def subtract(self, *num_s):
        self.sub_result = 0
        for value in num_s:
            self.sub_result += value
        self.result -= self.sub_result
        return self

md = MathDojo().add(2).add(2, 5).subtract(3, 2).result
print md

# PART 2  Support for lists and integers
class MathDojo2(object):
    def __init__(self):
        self.result = 0
    def add(self, *num_a):
        for value in num_a:
            if type(value) == list:
                for el in value:
                    self.result += el
            elif type(value) == int:
                self.result += value
        return self
    def subtract(self, *num_s):
        for value in num_s:
            if type(value) == list:
                for el in value:
                    self.result += el
            elif type(value) == int:
                self.result -= value
        return self

md2 = MathDojo2().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
print md2

# PART 3  Support for lists, tuples and integers
class MathDojo3(object):
    def __init__(self):
        self.result = 0
    def add(self, *num_a):
        for value in num_a:
            if isinstance(value, (list, tuple)):
                for el in value:
                    self.result += el
            elif isinstance(value, int):
                self.result += value
        return self
    def subtract(self, *num_s):
        for value in num_s:
            if isinstance(value, (list, tuple)):
                for el in value:
                    self.result -= el
            elif isinstance(value, int):
                self.result -= value
        return self

md3 = MathDojo3().add((1,2,3,4),[5,8,12,4],14).subtract((2,3),[6,9],7).result
print md3