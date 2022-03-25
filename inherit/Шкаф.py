class Wardrobe:
    def __init__(self, *args):
        self.data = args
    
    def __str__(self):
        return ' '.join(self.data)


class JustWardrobe(Wardrobe):
    def __str__(self):
        return ', '.join(self.data).capitalize() + '.'
    
    def __ne__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return len(self.data) != len(other.data)
        return True

    def __eq__(self, other):
        return not self != other

    def __le__(self, other):
        if self == other:
            return True
        return self < other

    def __ge__(self, other):
        if self == other:
            return True
        return other <= self

    def __lt__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return len(self.data) < len(other.data)
        if other.__class__.__name__ == 'MagicWardrobe':
            return True

    def __gt__(self, other):
        return other < self


class MagicWardrobe(Wardrobe):
    def __str__(self):
        return ', '.join([i.capitalize() for i in sorted(self.data)]) + '.'
    
    def __ne__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return len(self.data) != len(other.data)
        return True

    def __eq__(self, other):
        return not self != other

    def __le__(self, other):
        if self == other:
            return True
        return self < other

    def __ge__(self, other):
        if self == other:
            return True
        return other <= self

    def __lt__(self, other):
        if self.__class__.__name__ == other.__class__.__name__:
            return len(self.data) < len(other.data)
        if other.__class__.__name__ == 'JustWardrobe':
            return False

    def __gt__(self, other):
        return other < self
