# 길이가 다른 K개의 랜선을 길이가 같은 N개의 랜선으로 자르기 
# N개보다 많이 만드는 경우도 포함 , 최대 랜선 길이 구하기

import sys
input = sys.stdin.readline

K, N = map(int,input().split())

lan_lst = [int(input()) for _ in range(K)]

# print(lan_lst)

