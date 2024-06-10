import sys
input= sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    what = input().split()

    if what[0]=='top':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
    elif what[0]=='pop':
        if len(lst) ==0 :
            print(-1)
        else:
            print(lst.pop())
    elif what[0]=='size':
        print(len(lst))
    elif what[0]=='empty':
        if len(lst)==0 :
            print(1)
        else:
            print(0)
    elif what[0]=='push':
        lst.append(int(what[1]))