class Unicorn:
    def __init__(self, length, real):
        self.length, self.real = length, real
    
    def __iadd__(self, upd):
        self.length += upd[0]
        self.real += upd[1]
        self.length = min(10, self.length)
        self.length = max(0, self.length)
        self.real = min(100, self.real)
        self.real = max(1, self.real)
        return self
    
    def __add__(self, other):
        return Unicorn(min(10, self.length + other.length), min(100, self.real + other.real))
    
    def __floordiv__(self, m):
        return [Unicorn(self.length // m, self.real // m) for i in range(m)]
    
    def __str__(self):
        return 'Unicorn has corn of {} and degree of {}'.format(self.length, self.real)
    
    def __repr__(self):
        return 'Unicorn({}, {})'.format(self.length, self.real)
