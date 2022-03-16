class Talking:
    def __init__(self, name, time, themes=[]):
        self.name, self.time, self.themes = name, time, themes
    
    def add_theme(self, value):
        self.themes.append(value)
    
    def get_theme(self):
        if self.themes:
            return self.themes[0]
        return ''
    
    def change_theme(self):
        self.themes = self.themes[1:] + [self.themes[0]]
    
    def change_time(self, value):
        self.time += value
    
    def __str__(self):
        return "{}'s Conversation, main theme is {} for {} minutes".format(self.name, self.get_theme(), self.time)
    
    def __eq__(self, other):
        return (self.name, self.time, self.themes) == (other.name, other.time, other.themes)
    
    def __ne__(self, other):
        return not self == other
    
    def __lt__(self, other):
        if self == other:
            return False
        if self.time < other.time:
            return True
        elif self.time == other.time:
            if len(self.themes) < len(other.themes):
                return True
            elif len(self.themes) == len(other.themes):
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
