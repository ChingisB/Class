class Seat:
    #таким образом функция принимает произвольное кол-во аргументов
    #потому что нам нет необходимости хранит их отдельно
    def __init__(self, *args):
        self.args = list(map(str, args))
    #так можно сделать отображение корректным
    #для каждого класса наследника
    def __str__(self):
        return self.__class__.__name__ + '(' + ', '.join(self.args) + ')'

    def __repr__(self):
        return str(self)


class Chair(Seat):
    pass


class ArmChair(Seat):
    pass


class Stool(Seat):
    pass


class BagChair(Seat):
    pass
