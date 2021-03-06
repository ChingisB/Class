class VoltaicPile:
    next_value = {'Cu': 'cloth', 'Zn': 'cloth'}
    def __init__(self, values):
        self.values = values[:]
        self.i = 0
    
    def __len__(self):
        return len(self.values)
    
    def __getitem__(self, key):
        return self.values[key]
    
    def __setitem__(self, key, value):
        self.values[key] = value
    
    def append(self, value):
        if self.values[-1] == 'cloth':
            if self.values[-2] == 'Cu' and value == 'Zn':
                self.values.append(value)
            elif self.values[-2] == 'Zn' and value == 'Cu':
                self.values.append(value)
        elif value == self.next_value[self.values[-1]]:
            self.values.append(value)
    
    def __iter__(self):
        return iter(self.values)
    
    def __next__(self):
        self.i += 1
        return self.values[self.i - 1]
    
    def __str__(self):
        return '{} V'.format(''.join(self.values).count('CuclothZn') * 1.1)
