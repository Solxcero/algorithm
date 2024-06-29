import sys

input = sys.stdin.readline

i = 1

while True :
    L, P, V = map(int,input().split())
    if L == 0:
        break
    day1 = V//P*L
    if V%P >=  L :
        day2 = L
    else:
        day2 = V%P
    
    print(f'Case {i}: {day1+day2}')
    i += 1

'''
123 456 789
Case 1: 246
5 15 40
Case 2: 15
5 8 22
Case 3: 15
5 8 23
Case 4: 15
5 8 20
Case 5: 14
'''