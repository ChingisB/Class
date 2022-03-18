class Liked:
    def __init__(self, *args):
        self.emojis = [':)', ';)', ':(' ';(', '(', ')']
        self.fill(*args)
    
    def fill(self, *args):
        self.emotions = dict()
        for i in args:
            for j in self.emojis:
                if j in i:
                    self.emotions.setdefault(j, 0)
                    if j == ')':
                        self.emotions[j] += i.count(j) - i.count(':)') - i.count(';)')
                        continue
                    if j == '(':
                        self.emotions[j] += i.count(j) - i.count(':(') - i.count(';(')
                        continue
                    self.emotions[j] += i.count(j)
    
    def likes(self):
        ans = {}
        for i in self.emotions.keys():
            if not self.emotions[i]:
                continue
            ans[i] = self.emotions[i]
        return ans


class MiMiMi(Liked):
    def fill(self, *args):
        self.emotions = dict()
        self.emojis = [':)', ';)', ':(' ';(', '(', ')']
        for i in args:
            if 'cat' not in i and 'kitten' not in i:
                continue
            for j in self.emojis:
                if j in i:
                    self.emotions.setdefault(j, 0)
                    if j == ')':
                        self.emotions[j] += i.count(j) - i.count(':)') - i.count(';)')
                        continue
                    if j == '(':
                        self.emotions[j] += i.count(j) - i.count(':(') - i.count(';(')
                        continue
                    self.emotions[j] += i.count(j)

    def __init__(self, *args):
        self.emojis = [':)', ';)', ':(' ';(', '(', ')']
        self.fill(*args)


lines = ["What a cute kitten :):)", "I love it:)",
         "So pretty cat:))))", "See, kitty :)",
         "What happened to the cat ;("]
mi = MiMiMi(*lines)
print(mi.likes())