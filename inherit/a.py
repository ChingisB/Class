class Liked:
    def __init__(self, *args):
        self.emojis = [':)', ';)', ':(' ';(', '(', ')']
        self.acc = (' ')
        self.fill(*args)
    
    def fill(self, *args):
        self.emotions = dict()
        for i in args:
            flag = False
            for j in self.acc:
                if j in i:
                    flag = True
                    break
            if flag:
                continue
            for j in self.emojis:
                t = i.count(j)
                if j == ')':
                    t -= i.count(':)') + i.count(';)')
                if j == '(':
                    t -= i.count(':(') + i.count(';(')
                self.emotions.setdefault(j, 0)
                self.emotions[j] += t
    
    def likes(self):
        ans = {}
        for i in self.emotions.keys():
            if not self.emotions[i]:
                continue
            ans[i] = self.emotions[i]
        return ans


class MiMiMi(Liked):
    def __init__(self, *args):
        self.emojis = [':)', ';)', ':(' ';(', '(', ')']
        self.acc = ('cat', 'kitten')
        self.fill(*args)

lines = ["Hi, ;)!", "How are you))", "Well ;)?"]
lk = Liked(*lines)
print(lk.likes())