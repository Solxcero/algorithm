import sys
input = sys.stdin.readline

N = int(input())

time_table = []
for _ in range(N):
    s , f = map(int,input().split())
    time_table.append((s,f))

time_table.sort(key=lambda x:(x[1], x[0]))
print(time_table)

i = 0
count = 1

for j in range(1,N):
    if time_table[j][0] >= time_table[i][1]:
        count += 1
        i = j

print(count)


'''
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

> 4

2
4 4
1 4

> 2
'''