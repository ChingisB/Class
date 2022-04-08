class Board:
    def __init__(self, n, m, fill='0'):
        self.arr = []
        for i in range(n):
            self.arr.append([fill] * m)

    def __str__(self):
        return '\n'.join([''.join(i) for i in self.arr])


class Checker(Board):
    def __init__(self, n, fill1='0', fill2='1'):
        super().__init__(n, n, fill1)
        for i in range(n):
            begin = (i + 1) % 2
            for j in range(begin, n, 2):
                self.arr[i][j] = fill2


class Chess(Checker):
    def __init__(self):
        super().__init__(8, fill1='1', fill2='0')
        for i in range(8):
            self.arr[-2][i] = 'P'
        self.arr[-1][0], self.arr[-1][-1] = 'R', 'R'
        self.arr[-1][1], self.arr[-1][-2] = 'N', 'N'
        self.arr[-1][2], self.arr[-1][-3] = 'B', 'B'
        self.arr[-1][3], self.arr[-1][-4] = 'K', 'Q'
        for i in range(2):
            for j in range(8):
                self.arr[i][j] = self.arr[-i - 1][j].lower()

    def put_on(self, l1='', l2=''):
        for i in range(8):
            for j in range(8):
                if self.arr[i][j] == l1:
                    self.arr[i][j] = l2
                elif self.arr[i][j] == l1.lower():
                    self.arr[i][j] = l2.lower()


chess = Chess()
chess.put_on()
print(chess)