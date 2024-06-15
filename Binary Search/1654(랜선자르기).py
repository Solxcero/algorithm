# 길이가 다른 K개의 랜선을 길이가 같은 N개의 랜선으로 자르기 
# N개보다 많이 만드는 경우도 포함 , 최대 랜선 길이 구하기
# target = 11
# arr = 자르는 길이 


import sys
input = sys.stdin.readline

K, N = map(int,input().split())

lan_lst = [int(input()) for _ in range(K)]

left, right = 1, max(lan_lst)

def solution(lan_lst,N,left, right):
    print(left, right)
    if left > right:
        return right
    
    mid = (left + right) // 2
    
    lan_count = 0
    for l in lan_lst:
        lan_count += l//mid

    if lan_count < N:
        return solution(lan_lst,N,left, mid-1) 
    
    else:
        return solution(lan_lst,N,mid + 1, right)

print(solution(lan_lst,N,left,right))



'''
4 11
802
743
457
539

>200
'''