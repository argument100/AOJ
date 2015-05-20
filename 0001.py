# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0001

li = []

for n in range(10):
    li.append(int(raw_input()))

li.sort(reverse=True)

for i in li[0:3]:
    print i
