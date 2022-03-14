class ChairLeg:
    def __init__(self, n):
        self.length = n
    
    def __mul__(self, m):
        self.length *= m 
    
    def __rmul__(self, m):
        self.length *= m
    
    def __div__(self, m):
        self.length /= m
    
    def __mod__(self, m):
        return self.length % m


chl = ChairLeg(15)
chl * 3
print(chl.length)
2 * chl
print(chl.length)
print(chl % 7)