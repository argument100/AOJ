# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0002

import sys

for n in sys.stdin:
    i,j = map(int, n.split())
    print len(str(i + j))
