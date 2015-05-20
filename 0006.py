# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0006

st = raw_input()
li = ""
for x in range(len(st)):
    li = st[x] + li
print li

# 別の方法
# st = raw_input()
# print st[::-1]