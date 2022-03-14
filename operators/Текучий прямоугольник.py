class FlowingRectangle:
    def __init__(self, a, b):
        self.a, self.b, self.prop = a, b, (a, b)
    
    def get_width(self):
        return round(self.a, 2)
    
    def get_height(self):
        return round(self.b, 2)
    
    def __add__(self, other):
        area = self.a * self.b + other.a * other.b
        self.b = ((area * self.prop[1]) / self.prop[0]) ** 0.5
        self.a = area / self.b
    
    def __sub__(self, other):
        area = self.a * self.b - other.a * other.b
        if area <= 0:
            self.a, self.b = 0, 0
        else:
            self.b = ((area * self.prop[1]) / self.prop[0]) ** 0.5
            self.a = area / self.b
