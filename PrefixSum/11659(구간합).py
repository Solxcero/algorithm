import sys
input = sys.stdin.readline

N,M = map(int,input().split())

lst = list(map(int,input().split()))

sum_lst = [0] # 0번 인덱스 미리 입력
temp = 0 

# 구간 합 sum_lst에 추가 
for i in lst :
    temp += i 
    sum_lst.append(temp)

for _ in range(M):
    a,b = map(int,input().split())
    print(sum_lst[b]-sum_lst[a-1])
