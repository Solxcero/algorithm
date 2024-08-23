import sys

input = sys.stdin.readline


N = int(input())
arrN = list(map(int,input().split()))
M = int(input())
arrM = list(map(int,input().split()))

arrN.sort()

def find_num(target):
    left, right = 0, N-1
    while left <= right :
        mid = (left + right)//2
        
        if arrN[mid] == target:
            return 1
        
        elif arrN[mid] > target:
            right = mid - 1
        
        else:
            left = mid + 1
    return 0
            
for target in arrM:
    print(find_num(target))