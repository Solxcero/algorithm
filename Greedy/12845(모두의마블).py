import sys
input = sys.stdin.readline

n = int(input())

lvl_lst = list(map(int,input().split()))
lvl_lst.sort(reverse=True)

gold_sum = 0
lvl = lvl_lst[0]

for i in range(1,n):
    tmp = lvl + lvl_lst[i]
    print(f'합치기 : {tmp}')
    gold_sum += tmp
    print(f'누적합 : {gold_sum}')
    lvl = max(lvl,lvl_lst[i] )

print(gold_sum)

'''
3
40 30 30
'''