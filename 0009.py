# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0009

import sys
import math
for x in sys.stdin:
    x = int(x)
    if x == 1:
        print 0
        continue
    li = []
    limit = int(math.sqrt(x))+1
    ans = 0
    append = li.append
    for i in range(0,x+1):
        if i == 0 or i == 1:
            append(0)
        else:
            append(1)
    cnt = 2
    while 2*cnt <= x:
        li[2*cnt] = 0
        cnt = cnt+1
    for i,v in enumerate(li[3:]):
        i = i + 3
        if limit < i:
            break
        elif v == 1:
            cnt = 3
            dele = cnt*i
            while dele < x:
                if li[dele] == 1:
                    li[dele] = 0
                cnt = cnt+2
                dele = cnt*i
    for n in li:
        if n == 1:
            ans = ans + 1
    print ans
