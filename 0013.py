# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0013

import sys
arr = []
append = arr.append
for x in sys.stdin:
    x = int(x)
    if x == 0:
        print(arr.pop())
    else:
        append(x)
