import sys


inf = 123456789

class Expression:
    d = []
    k = 0
    def __init__(self, k = 0):
        self.k = k
        self.d = []
        for i in range(k + 1):
            self.d.append(inf)
    def __add__(self, other):
        ans = Expression(self.k)
        for i in range(self.k + 1):
            ans.d[i] = min(self.d[i], other.d[i])
        return ans
    def __mul__(self, other):
        ans = Expression(self.k)
        for i in range(self.k + 1):
            for m in range (i + 1):
                ans.d[i] = min(ans.d[i], self.d[m] + other.d[i - m])
        return ans
    def star(self):
        self.d[0] = 0
        for l in range(1, self.k):
            for i in range(1, self.k - l + 1):
                self.d[l + i] = min(self.d[l + i], self.d[l] + self.d[i])
    def ans(self):
        if self.d[self.k] < inf:
            return str(self.d[self.k])
        else:
            return "inf"


def solve():
    input_file = sys.stdin
    output_file = sys.stdout
    stack = []
    str1 = input_file.read()
    str2 = str1.split(" ")
    string = str2[0]
    x = str2[1]
    k = int(str2[2])
    for c in string:
        if c == "+":
            exp1 = stack.pop()
            exp2 = stack.pop()
            stack.append(exp1 + exp2)
        elif c == ".":
            exp1 = stack.pop()
            exp2 = stack.pop()
            stack.append(exp1 * exp2)
        elif c == "*":
            exp = stack.pop()
            exp.star()
            stack.append(exp)
        else:
            exp = Expression(k)
            if c == x:
                exp.d[1] = 1
            else:
                exp.d[0] = 1
            stack.append(exp)
    exp = stack.pop()
    output_file.write(exp.ans())
    input_file.close()
    output_file.close()

solve()