class ModifiedString:
    def __init__(self, string):
        self.string = string
    
    def __add__(self, other):
        return ModifiedString(self.string + other)
    
    def __radd__(self, other):
        return ModifiedString(other + self.string)
    
    def __sub__(self, other):
        ans = ''
        for i in self.string.lower():
            if i in other.lower():
                continue
            ans += i
        return ModifiedString(ans)
    
    def __rsub__(self, other):
        ans = ''
        for i in other.lower():
            if i in self.string.lower():
                continue
            ans += i
        return ModifiedString(ans)
    
    def __str__(self):
        return self.string


ms_1 = ModifiedString('My heart in the Highland')
ms_2 = 'my heart is not here'
print(ms_1 - ms_2)
print(ms_2 - ms_1)