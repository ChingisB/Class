class Rewrite:
    def __init__(self, infile, outfile):
        self.infile, self.outfile = infile, outfile
    
    def done(self):
        with open(self.infile, encoding='utf8') as infile, open(self.outfile, 'w') as out:
            for i in infile.readlines():
                print(i, file=out, end='')


class Calculus(Rewrite):
    def five_per_line(self):
        ans = []
        infile = open(self.infile, encoding='utf8')
        out = open(self.outfile, 'w')
        for i in infile.readlines():
            for j in [int(k) for k in i.rstrip().split()]:
                ans.append(j)
        ans.sort()
        ans = list(map(str, ans))
        for i in range(5, len(ans), 5):
            print(*ans[i - 5: i], file=out)
        print(*ans[len(ans) - len(ans) % 5:], file=out)
        infile.close()
        out.close()


class Align(Rewrite):
    def to_right(self):
        with open(self.infile) as infile, open(self.outfile, 'w') as out:
            data = [i.rstrip() for i in infile.readlines()]
            maximum = max(data, key=len)
            for i in data:
                print(' ' * (len(maximum) - len(i)) + i, file=out)