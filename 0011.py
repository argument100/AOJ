# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0011

w = int(raw_input())
n = int(raw_input())
arr = []
append = arr.append
for i in range(w):
    append(i+1)

for a in xrange(n):
    a1,a2 = map(int, raw_input().split(","))
    b1 = arr[a1 - 1]
    b2 = arr[a2 - 1]
    arr[a1-1] = b2
    arr[a2-1] = b1

for x in arr:
    print(x)