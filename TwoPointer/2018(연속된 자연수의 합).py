import sys
input = sys.stdin.readline

N = int(input())

s,e = 1, 1 # 시작 인덱스, 종료 인덱스 
cnt = 1 #정수 자기 자신포함시킨 상태로 초기화
sum = 1 #1부터 합 시작 

while e != N : # 종료 인덱스가 N 자기 자신이 되기 전까지 수행
    if sum == N : 
        # 합 성립 
        #print(list(range(s,e+1)),'+')
        cnt += 1
        e += 1
        sum += e
    elif sum > N :
         # N 초과할 경우 시작인덱스를 빼줌
        #print(list(range(s,e+1)))
        sum -= s 
        s+=1
    else: #elif sum < N : 
        #print(list(range(s,e+1)))
        e += 1
        sum += e
print(cnt)