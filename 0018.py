# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0018

n = map(int, raw_input().split())
print " ".join(map(str,sorted(n, reverse=True)))