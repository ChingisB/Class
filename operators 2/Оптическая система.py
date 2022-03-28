class OpticSystem:
    def __init__(self, arr):
        self.arr = arr[:]
    
    def __add__(self, other):
        return OpticSystem(self.arr + other.arr)
    
    def __iadd__(self, value):
        self.arr += value
        return self
    
    def append(self, value):
        self.arr.append(value)
    
    def __iter__(self):
        return iter(self.arr)
    
    def __delitem__(self, key):
        del self.arr[key]
    
    def __setitem__(self, key, value):
        self.arr[key] = value
    
    def __getitem__(self, key):
        return self.arr[key]
    
    def __len__(self):
        return len(self.arr)
    
    def __call__(self, value):
        if value == 0:
            return None
        return round(value / (sum(self.arr) * value - 1), 4)

    def __rshift__(self, n):
        n = n % (len(self.arr))
        self.arr = self.arr[len(self.arr) - n:] + self.arr[:len(self.arr) - n]
    
    def __lshift__(self, n):
        n = n % (len(self.arr))
        self.arr = self.arr[n:] + self.arr[:n]
    
    def __eq__(self, other):
        return sum(self.arr) == sum(other.arr) and len(self) == len(other)
    
    def __ne__(self, other):
        return not self == other
    
    def __lt__(self, other):
        if sum(self.arr) == sum(other.arr):
            return len(self) < len(other)
        return sum(self.arr) < sum(other.arr)
    
    def __gt__(self, other):
        if self == other:
            return False
        return not self < other
    
    def __le__(self, other):
        if self == other:
            return True
        return self < other
    
    def __ge__(self, other):
        if self == other:
            return True
        return self > other
