class LettersRhombus:
    def __init__(self, letter, empty=' '):
        self.matrix = []
        self.letter = letter
        for i in range(ord(letter) - ord('A') + 1):
            t = []
            for j in range(2 * (ord(letter) - ord('A')) + 1):
                t.append(empty)
            self.matrix.append(t)
        self.fill()

    def fill(self):
        symb = 'A'
        posy, posx = 0, 0
        while ord(symb) <= ord(self.letter):
            self.matrix[posx][len(self.matrix[0]) // 2 + posy] = symb
            self.matrix[posx][len(self.matrix[0]) // 2 - posy] = symb
            posy, posx = posx + 1, posy + 1
            symb = chr(ord(symb) + 1)
        for i in self.matrix[-2:-len(self.matrix) - 1:-1]:
            self.matrix.append(i)

    def rows(self):
        return [''.join(i) for i in self.matrix]

    def cols(self):
        ans = []
        for i in range(len(self.matrix)):
            t = []
            for j in range(len(self.matrix)):
                t.append(self.matrix[j][i])
            ans.append(''.join(t))
        return ans
