class ClassicalMechanics:
    def __init__(self, v):
        self.v = v

    def __call__(self, v1):
        return self.v + v1
    
    def __str__(self):
        return 'Object {}, velocity {} c'.format(self.__class__.__name__, self.v)
    

class SpecialTheoryRelativity(ClassicalMechanics):
    def __call__(self, v1):
        if self.v >= 0.1 or v1 >= 0.1:
            c = 3 * (10 ** 8)
            return (self.v + v1) / (1 + self.v * v1)
        return super().__call__(v1)
