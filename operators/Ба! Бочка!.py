class Butterfly:
    def __init__(self, vol):
        self.vol = vol
        self.full = 0
    
    def __iadd__(self, num): 
        self.full = min(self.vol, self.full + num)
        self.full = max(0, self.full)
        return self
    
    def __add__(self, other):
        return Butterfly(self.vol + other.vol)
    
    def __floordiv__(self, num):
        if self.vol % num == 0:
            return [Butterfly(self.vol // num) for i in range(num)]
        return [Butterfly(self.vol // num) for i in range(num)] + [Butterfly(self.vol % num)]
    
    def __str__(self):
        return 'Volume: {}, content: {}'.format(self.vol, self.full)
    
    def __repr__(self):
        return 'Butterfly({})'.format(self.vol)
