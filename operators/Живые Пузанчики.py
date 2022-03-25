class Chubby:
    def __init__(self, name, num):
        self.name = name
        self.num = num
    
    def __iadd__(self, m):
        self.num = max(0, self.num + m)
        return self
    
    def __add__(self, other):
        return Chubby(self.name + '-' + other.name, self.num + other.num)
    
    def __mul__(self, m):
        ans = []
        for i in range(m):
            ans.append(Chubby(self.name, self.num // m))
        return ans
    
    def __repr__(self):
        return 'Chubby("{}", {})'.format(self.name, self.num)
    
    def __str__(self):
        return 'Chubby {} has {} coins'.format(self.name, self.num)
