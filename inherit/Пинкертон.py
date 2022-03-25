class Storm:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return "Storm('{}')".format(self.name)


class ThunderAndLightning(Storm):
    def __init__(self, dict, name='Irma'):
        self.name = name
        self.dict = dict
    
    def __getitem__(self, key):
        return self.dict[key]
    
    def __setitem__(self, key, value):
        self.dict[key] = value
    
    def __iter__(self):
        return iter(self.dict.keys())
    
    def __repr__(self):
        return 'ThunderAndLightning({})'.format(self.dict)
    
    def items(self):
        return self.dict.items()
