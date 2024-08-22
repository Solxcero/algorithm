import sys
input = sys.stdin.readline
N = int(input())
arrN = list(map(int,input().split()))
M = int(input())
arrM = list(map(int,input().split()))

# 1. bisect 함수 사용
from bisect import bisect_left, bisect_right
arrN.sort()

def count_by_range(a, left, right):
    rigt_idx = bisect_right(a,right)
    left_idx = bisect_left(a, left)
    return rigt_idx - left_idx

for i in range(M):
    print(count_by_range(arrN,arrM[i],arrM[i]),end=' ')
    
    
# 2. Counter 내장함수 사용
from collections import Counter

count = Counter(arrN)

for i in range(M):
    if arrM[i] in count:
        print(count[arrM[i]],end =' ')
    else:
        print(0, end = ' ')

# 3. 딕셔너리사용
dic = {}

for i in arrN:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in arrM:
    if i in dic:
        print(dic[i],end = ' ')
    else:
        print(0, end = ' ')



'''
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10

3 0 0 1 2 0 0 2
'''