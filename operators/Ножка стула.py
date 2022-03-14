class ChairLeg:
    def __init__(self, n):
        self.length = n
    
    def __mul__(self, m):
        self.length *= m 
    
    def __rmul__(self, m):
        self.length *= m
    
    def __truediv__(self, m):
        self.length /= m
    
    def __mod__(self, m):
        return self.length % m
    
    def __floordiv(self, m):
        self.n = self.n // m
