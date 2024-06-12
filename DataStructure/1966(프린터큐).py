# 문서 배열 과 중요도 배열 주어짐
# 원하는 문서의 위치를 지속적으로 업데이트 해줄 필요가 있음

import sys
from collections import deque
input = sys.stdin.readline


## 1
cases = int(input())
for _ in range(cases):
    N, M = map(int,input().split())
    docs_dq = deque(map(int,input().split()))
    done = 0
    i = 0
    while True:
        
        if i+1 == len(docs_dq):
            if M == 0:
                print(done+1)
                break
            
            else:
                docs_dq.popleft()
                M -= 1
                done +=1 
                i = 0
                print('now : ', docs_dq,M)
        
        # 이 조건문은 이 위치에 있어야 함;;
        if len(docs_dq) == 1:
            print(done+1)
            break 
                
        if docs_dq[0] >= docs_dq[i+1]:
            i += 1
        else:
            docs_dq.append(docs_dq.popleft())
            if M == 0 :
                M = len(docs_dq)-1
            else:
                M -= 1
            i = 0
            print(docs_dq,M)

## 2
# test_case = int(input())

# for _ in range(test_case):
#     N, target = map(int, input().split())
#     print_queue = list(map(int, input().split()))
#     level_stack = sorted(print_queue)
#     result = 0
#     index = 0
#     while print_queue[target]:
#         if level_stack[-1] == print_queue[index]:
#         # if print_queue[index] and level_stack[-1] == print_queue[index]:
#             print_queue[index] = False
#             result += 1
#             level_stack.pop()
#         index += 1
#         if index == len(print_queue):
#             index = 0
#     print(result)


## 3
# t = int(input())

# for _ in range(t):
#     n, m = map(int, input().split())
#     pop_num = []

#     queue = deque([i+1 for i in range(n)])
#     find_num = queue[m]
#     imp_q = deque(map(int, input().split()))

#     while True:
#         if len(imp_q) == 0 :
#             break
    
#         max_idx = imp_q.index(max(imp_q))

#         if max_idx != 0:
#             queue.rotate(-1)
#             imp_q.rotate(-1)
#             continue

#         elif max_idx == 0:
#             pop_num.append(queue.popleft())
#             imp_q.popleft()
#             continue

#     for num in pop_num :
#         if find_num == num :
#             print(pop_num.index(num) + 1)
    
'''
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1

2
9 3
4 3 2 2 3 5 2 1 3
4 1
2 1 4 3


1
100 0
1 2 3 4 5 6 7 8 9 2 2 3 4 5 6 7 8 9 2 2 3 4 5 6 7 8 9 2 2 3 4 5 6 7 8 9 2 2 3 4 5 6 7 8 9 2 2 3 4 5 6 7 8 9 2 2 3 4 5 6 7 8 9 2 2 3 4 5 6 7 8 9 2 2 3 4 5 6 7 8 9 2 2 3 4 5 6 7 8 9 5 5 5 5 5 5 5 5 5 5

'''