class AbstractCat:
    def __init__(self):
        self.food = 0
        self.weight = 0

    def eat(self, num):
        num += self.food
        self.food = num % 10
        self.weight = min(100, self.weight + num // 10)
    
    def __str__(self):
        return '{} ({})'.format(self.__class__.__name__, self.weight)


class Kitten(AbstractCat):
    def __init__(self, weight):
        super().__init__()
        self.weight += weight
    
    def meow(self):
        return 'meow'
    
    def sleep(self):
        return 'Snore' * (self.weight // 5)


class Cat(Kitten):
    def __init__(self, weight, name):
        super().__init__(weight)
        self.name = name
    
    def meow(self):
        return 'MEOW...'
    
    def get_name(self):
        return self.name
    
    def catch_mice(self):
        return 'Got it!'
