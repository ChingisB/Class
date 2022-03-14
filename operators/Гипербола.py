class Hyperbole:
    def __init__(self, a, b):
        self.a, self.b = a, b
    
    def __str__(self):
        return 'y = {} + {}/x'.format(self.a, self.b)
    
    def __repr__(self):
        return 'Hyp({}, {})'.format(self.a, self.b)
    
    def __call__(self, x):
        if x == 0:
            return None
        return round(self.a + self.b / x, 6)

hyp = Hyperbole(2.5, 3)
print(hyp(2))
print(hyp.__repr__())
print(hyp)