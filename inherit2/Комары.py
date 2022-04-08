class Mosquito:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return '{}, {} days'.format(self.__class__.__name__, self.age)


class MaleMosquito(Mosquito):
    def __init__(self, age):
        super().__init__(age)
        self.feed = 'nectar'
        self.lives = 'on land'

    def hearing(self):
        return 'I hear and see everything {}'.format(self.lives)


class FemaleMosquito(Mosquito):
    def __init__(self, age):
        self.age = age
        self.feed = 'blood'
        self.lives = 'on land'

    def squeak(self):
        name = self.feed
        return 'The thin squeak of a mosquito after eating {}'.format(name)


class MosquitoLarva(MaleMosquito, FemaleMosquito):
    def __init__(self, age):
        self.age = age
        self.feed = 'algae'
        self.lives = 'in water'
