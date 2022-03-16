class EpicHero:
    def __init__(self, name, wins, weapons=[]):
        self.name, self.wins, self.weapons = name, wins, weapons
    
    def add_win(self):
        self.wins += 1
    
    def add_weapon(self, value):
        self.weapons.append(value)
    
    def get_weapon(self):
        if self.weapons:
            return self.weapons[0]
        return ''
    
    def del_weapon(self, value):
        if value in self.weapons:
            self.weapons.remove(value)
    
    def __str__(self):
        return 'Epic Hero {}, {}'.format(self.name, self.wins)
    
    def __eq__(self, other):
        return (self.name, self.wins, len(self.weapons)) == (other.name, other.wins, len(other.weapons))
    
    def __ne__(self, other):
        return not self == other
    
    def __lt__(self, other):
        if self == other:
            return False
        if self.wins < other.wins:
            return True
        elif self.wins == other.wins:
            if len(self.weapons) < len(other.weapons):
                return True
            elif len(self.weapons) == len(other.weapons):
                if len(self.name) > len(other.name):
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
    
    def __repr__(self):
        return "EpicHero('{}', {}, {})".format(self.name, self.wins, sorted(self.weapons))
