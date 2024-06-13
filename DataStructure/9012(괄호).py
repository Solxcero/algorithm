import sys 
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    temp = []
    s_arr = input().strip()
    
    for s in s_arr:
        if s == '(':
            temp.append(s)
        elif s == ')':
            if temp:
                temp.pop()
            else:
                temp.append(')')
                break
    
    print('YES' if not temp else 'NO')





'''
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(


3
((
))
())(()
'''