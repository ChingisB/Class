from operator import add


class Service:
    def __init__(self, address, id):
        self.dict = {}
        self.dict['address'], self.dict['id'] = address, id

    def arrival_time(self):
        return len(self.dict['address'])

    def get(self):
        return self.dict


class Ambulance(Service):
    def __init__(self, address, id, mode, severity):
        super().__init__(address, id)
        self.dict['mode'], self.dict['severity'] = mode, severity


class FireFighters(Service):
    def __init__(self, address, id, mode, victims):
        super().__init__(address, id)
        self.dict['mode'], self.dict['victims'] = mode, victims


class Police(FireFighters):
    def __init__(self, address, id, mode, victims, armament_required):
        super().__init__(address, id, mode, victims)
        self.dict['armament_required'] = armament_required
