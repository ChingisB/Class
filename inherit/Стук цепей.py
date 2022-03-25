class Sound:
    def __init__(self, sound='zing'):
        self.sound = sound

    def __repr__(self):
        return "Sound('{}')".format(self.sound)


class ChainRattle(Sound):
    def __init__(self, n, *args):
        self.container = []
        for i in range(n):
            if i < len(args):
                self.container.append(args[i])
                continue
            self.container.append('zing')

    def __getitem__(self, key):
        return self.container[key]
    
    def __setitem__(self, key, value):
        self.container[key] = value
    
    def __delitem__(self, key):
        del self.container[key]
    
    def append(self, value):
        self.container.append(value)
        
    def __iter__(self):
        return iter(self.container)
    
    def __repr__(self):
        t = []
        k = len(self.container)
        for i in self.container:
            t.append("'" + i + "'")
        return "ChainRattle({}, {})".format(k, ', '.join(t))
