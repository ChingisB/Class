class FastFibonacci:
    values = [0, 1]
    
    def __call__(self, n):
        while len(self.values) < n + 1:
            self.values.append(self.values[-1] + self.values[-2])
        return self.values[-1]