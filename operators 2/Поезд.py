class Wagon:
    def __init__(self, n):
        self.n = n
    
    def get_number(self):
        return self.n
    
    def __str__(self):
        return '№{}'.format(self.n)


class Train:
    def __init__(self, n, wagons=[]):
        self.n, self.wagons = n, wagons
    
    def get_number(self):
        return self.n
    
    def get_wagons(self):
        return self.wagons
    
    def append(self, item):
        self.wagons.append(item)
    
    def __len__(self):
        return len(self.wagons)
    
    def __str__(self):
        return 'Train {} has {} wagon'.format(self.get_number(), len(self))
    
    def __getitem__(self, key):
        return self.wagons[key]
    
    def __setitem__(self, key, value):
        self.wagons[key] = value
    
    def __delitem__(self, key):
        if key == len(self) - 1:
            self.wagons.pop(key)
    
    def __iter__(self):
        return iter(self.wagons)
