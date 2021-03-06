class PearsBasket:
    def __init__(self, n):
        self.n = n
    
    def __floordiv__(self, m):
        if not self.n % m:
            return [PearsBasket(self.n // m) for i in range(m)]
        return [PearsBasket(self.n // m) for i in range(m)] + [PearsBasket(self.n % m)]
    
    def __mod__(self, m):
        return self.n % m
    
    def __add__(self, other):
        return PearsBasket(self.n + other.n)
    
    def __sub__(self, m):
        self.n = max(0, self.n - m)
    
    def __str__(self):
        return str(self.n)
    
    def __repr__(self):
        return 'PearsBasket({})'.format(self.n)
