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


# 다른 풀이 : if 조건 one line 
# def process_command(stack, command):
    
#     order = command[0]
    
#     if order == "push":
#         stack.append(int(command[1]))
#         return None
#     elif order == "pop":
#         return stack.pop() if stack else -1
#     elif order == "size":
#         return len(stack)
#     elif order == "empty":
#         return 0 if stack else 1
#     elif order == "top":
#         return stack[-1] if stack else -1