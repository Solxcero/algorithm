# 절단기 높이 H (0~H)
# if treeHeight > H : treeHeight - H 만큼 잘림
# if            <   : 안잘림
# 나무를 자른 뒤 나무들의 높이 , 상근이가 들고가는 나무길이
# 적어도 M 미터의 나무를 집에 가져가기 위한 절단기 높이 최댓값
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
# 나무 높이의 합은 항상 M보다 크거나 같음
tree = list(map(int,input().split()))

left , right = 0, max(tree)
while left <= right:
    mid = (left + right)// 2
    
    total_cut = 0
    for t in tree:
        if t > mid:
            total_cut += t - mid
    
    # 높이 더 내려야함
    if total_cut < M :
        right = mid -1
        
    else:
        left = mid + 1
        
print(right)
    
