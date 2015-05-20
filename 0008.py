# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0008

while True:
    try:
        n = int(raw_input())
        count = 0
        for a in range(10):
            if n > 36:
                break
            if a < n-27:
                continue
            for b in range(10):
                if a+b < n-18:
                    continue
                for c in range(10):
                    if a+b+c < n-9:
                        continue
                    for d in range(10):
                        if n == a+b+c+d:
                            count = count+1
        print count
    except Exception:
        break
