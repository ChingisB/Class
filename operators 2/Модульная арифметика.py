class ModularArithmetic:
    def __init__(self, num, mode):
        self.mode, self.num = mode, num % mode
    
    def __add__(self, other):
        if self.mode == other.mode:
            return ModularArithmetic((self.num + other.num) % self.mode, self.mode)
    
    def __sub__(self, other):
        if self.mode == other.mode:
            return ModularArithmetic((self.num - other.num) % self.mode, self.mode)
    
    def __call__(self, n):
        return n // self.mode
    
    def __rshift__(self, n):
        return ModularArithmetic((self.num + n) % self.mode, self.mode)
    
    def __lshift__(self, n):
        return ModularArithmetic((self.num - n) % self.mode, self.mode)
    
    def __str__(self):
        return "{}({})".format(self.num, self.mode)
    
    def __repr__(self):
        return str(self)
