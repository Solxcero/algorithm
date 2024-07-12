def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
            
# from collections import deque
# def solution(priorities, location):
#     dq = deque(priorities)
#     loc = deque([0]*len(dq))
#     loc[location] = 1
#     answer = 0
    
#     while dq :
#         p = dq.popleft()
#         l = loc.popleft()
#         if len(dq) > 1 and p < max(dq):
#             dq.append(p)
#             loc.append(l)
            
#         else:
#             answer += 1
            
#             if l == 1:
#                 break

#     return answer