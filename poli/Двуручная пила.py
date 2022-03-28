class TwoHandedSawUp:
    def __init__(self, arr):
        self.arr = arr

    def sawing(self):
        self.arr.sort()
        t1 = self.arr[:int((len(self.arr) - 1) / 2) + 1:]
        t2 = self.arr[int((len(self.arr) - 1) / 2) + 1:]
        pos = 0
        for i in t1:
            t2.insert(pos, i)
            pos += 2
        self.arr = t2
        return self.arr

    def get_list(self):
        return self.arr


class TwoHandedSawDown:
    def __init__(self, arr):
        self.arr = arr

    def sawing(self):
        self.arr.sort()
        self.arr = self.arr[::-1]
        t1 = self.arr[:int((len(self.arr) - 1) / 2) + 1:]
        t2 = self.arr[int((len(self.arr) - 1) / 2) + 1:]
        pos = 1
        for i in t2:
            t1.insert(pos, i)
            pos += 2
        self.arr = t1
        return self.arr

    def get_list(self):
        return self.arr


def print_hist(array):
    for i in array:
        print('*' * int(i))
