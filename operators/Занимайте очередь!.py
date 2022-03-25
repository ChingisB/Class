class Queue:
    def __init__(self):
        self.q = []
    
    def add(self, value):
        self.q.append(value)
        return 'done'
    
    def remove(self):
        if self.q:
            return self.q.pop(0)
    
    def len(self):
        return len(self.q)
    
    def last(self):
        if self.q:
            return self.q[-1]
    
    def first(self):
        if self.q:
            return self.q[0]
    
    def clear(self):
        self.q.clear()
        return 'done'
