# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0005

while True:
    try:
        a, b = map(int, raw_input().split())
        n, m = a, b
        while not(n == m):
            ma = max(n,m)
            mi = min(n,m)
            ma = ma - mi
            n, m = ma, mi
        print str(n) + " " + str(a*b/n)
    except Exception:
        break