class Dragonfly:
    def __init__(self, n):
        self.n = n
    
    def __iadd__(self, m):
        self.n += m
        self.n = max(1, self.n)
        self.n = min(30, self.n)
        return self
    
    def __add__(self, other):
        return Dragonfly(min(30, self.n + other.n))
    
    def __truediv__(self, m):
        if self.n // m == 0:
            return []
        return [Dragonfly(self.n // m) for i in range(m)]
    
    def __str__(self):
        return "Dragonfly with a height of {}".format(self.n)
    
    def __repr__(self):
        return 'Dragonfly({})'.format(self.n)
