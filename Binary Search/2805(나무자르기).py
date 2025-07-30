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
    print(left, mid, right)

    total_cut = 0
    for t in tree:
        if t > mid:
            total_cut += t - mid
            
    
    # 높이 더 내려야함
    print(total_cut)
    if total_cut < M :
        right = mid -1
    else:
        left = mid + 1
        
print(right)

'''    
4 7
20 15 10 17

15
'''

# 풀이 2: 재귀
# def get_cut_wood(height, tree):
#     total_cut = 0
#     for t in tree:
#         if t > height:
#             total_cut += t - height
#     return total_cut

# def find_max_height(left, right, tree, M):
#     if left > right:
#         return right
    
#     mid = (left + right) // 2
#     total_cut = get_cut_wood(mid, tree)
    
#     if total_cut < M:
#         return find_max_height(left, mid - 1, tree, M)
#     else:
#         return find_max_height(mid + 1, right, tree, M)

# N, M = map(int, input().split())
# tree = list(map(int, input().split()))


# 풀이 3: Counter
# import sys
# from collections import Counter

# input = sys.stdin.readline

# N, M = map(int, input().split())
# heights = Counter(map(int, input().split()))

# start, end = 1, max(heights)
# while start <= end:
#     mid = (start + end) // 2

#     cutted = sum([(h-mid) * i for h, i in heights.items() if h > mid])

#     if cutted < M:
#         end = mid - 1
#     else:
#         start = mid + 1

# print(end)