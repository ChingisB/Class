class Knight:
    def __init__(self, name, weight, weapons=[]):
        self.name, self.weight, self.weapons = name, weight, weapons
    
    def overturn(self):
        self.name = self.name[::-1].capitalize()
        self.weapons = self.weapons[1:] + [self.weapons[0]]
    
    def add_weight(self, value):
        self.weight = max(0, self.weight + value)
    
    def add_weapon(self, value):
        self.weapons.append(value)
    
    def get_weapon(self):
        if self.weapons:
            return self.weapons[0]
        return ''
    
    def __str__(self):
        return 'Knight {}, weapon {}, {}'.format(self.name, self.get_weapon(), self.weight)
    
    def __eq__(self, other):
        return (self.name, self.weight, self.weapons) == (other.name, other.weight, other.weapons)
    
    def __ne__(self, other):
        return not self == other
    
    def __lt__(self, other):
        if self == other:
            return False
        if self.weight < other.weight:
            return True
        elif self.weight == other.weight:
            if len(self.weapons) < len(other.weapons):
                return True
            elif len(self.weapons) == len(other.weapons):
                if self.name < other.name:
                    return True
                return False
            return False
        return False
    
    def __gt__(self, other):
        if self == other:
            return False
        return other < self
    
    def __le__(self, other):
        if self == other:
            return True
        return self < other
    
    def __ge__(self, other):
        return other <= self
