class Transport:
    pass


class WaterTransport(Transport):
    pass


class Boats(WaterTransport):
    pass


class Yachts(WaterTransport):
    pass


class CruiseShips(WaterTransport):
    pass


class WaterCargoTransport(WaterTransport):
    pass


class Aircarafts(Transport):
    pass


class Planes(Aircarafts):
    pass


class Helicopters(Aircarafts):
    pass


class Airships(Aircarafts):
    pass


class Ballons(Aircarafts):
    pass


class LandTransport(Transport):
    pass


class RailwayTransport(LandTransport):
    pass


class BusTransport(LandTransport):
    pass


class CargoTransport(LandTransport):
    pass


class PrivateVehicles(LandTransport):
    pass


class SpaceTransport(Transport):
    pass


class SpacePassengerTransport(SpaceTransport):
    pass


class SpaceCargoTransport(SpaceTransport):
    pass