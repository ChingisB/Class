class Fish:
    def swim(self):
        return 'swim'
    
    def dive(self):
        return 'dive'
    
    def breathe_with_gills(self):
        return 'breathe_with_gills'


class LandAnimal:
    def walk_on_land(self):
        return 'walk_on_land'

    def breathe_air(self):
        return 'breathe_air'

    def feed_cubs(self):
        return 'feed_cubs'


class Whale(Fish, LandAnimal):
    def breathe_with_gills(self):
        return
    
    def walk_on_land(self):
        return
    
    def filter_food(self, array, n):
        return list(filter(lambda x: x <= n, array))
