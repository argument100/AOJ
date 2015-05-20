# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0007

import math

n = int(raw_input())
s = 100000
for x in range(n):
    s = int(math.ceil((s * 1.05) / 1000) * 1000)
print s