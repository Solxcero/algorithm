import sys
input = sys.stdin.readline

N = int(input())
p_lst = list(map(int,input().split()))

p_lst.sort()
# print(p_lst)
min_time = 0
min_sum_time = 0
for p in p_lst:
    min_time += p
    min_sum_time += min_time
print(min_sum_time)
'''
5
3 1 4 3 2
'''