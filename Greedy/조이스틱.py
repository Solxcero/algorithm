def solution(name):
    # 1. 커서 위아래 이동(그리디)
    # A : 65, Z: 90
    moves = 0 
    for i in range(len(name)):
        if name[i] != 'A':
            min_move = min((ord(name[i]) - 65), (91 - ord(name[i])))
            print(f"{name[i]}:{ord(name[i])}, A-> {ord(name[i]) - 65} , <-A {91 - ord(name[i])} | min : {min_move}")
            moves += min_move

    # 2. 커서 좌우 이동(.완전 탐색..?)
    min_move = len(name) - 1  # 초기값: 그냥 오른쪽으로 쭉 가는 경우
    for i in range(len(name)):
        next_idx = i + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1

        distance = (i * 2) + (len(name) - next_idx)
        alt_distance = i + ((len(name) - next_idx) * 2)

        min_move = min(min_move, distance, alt_distance)

    return moves+min_move

test_case = ["AAA","JAN","JEROEN","BABAAAAAAAAAB"] #,"JAAACAA","JAACAA","AACA", "CAAACACAAC",
for test in test_case:
    print(f'word : {test}')
    print(solution(test))
    print('====================')
"""
word : AAA
0
====================
word : JAN
J:74, A-> 9 , <-A 17 | min : 9
N:78, A-> 13 , <-A 13 | min : 13
23
====================
word : JEROEN
J:74, A-> 9 , <-A 17 | min : 9
E:69, A-> 4 , <-A 22 | min : 4
R:82, A-> 17 , <-A 9 | min : 9
O:79, A-> 14 , <-A 12 | min : 12
E:69, A-> 4 , <-A 22 | min : 4
N:78, A-> 13 , <-A 13 | min : 13
56
====================
word : BABAAAAAAAAAB
B:66, A-> 1 , <-A 25 | min : 1
B:66, A-> 1 , <-A 25 | min : 1
B:66, A-> 1 , <-A 25 | min : 1
7
"""
# 다른 풀이 : 위아래 탐색이랑 좌우탐색 합쳐서 
# def solution(name):
#     # A : 65, Z: 90
#     moves = 0 
#     min_move = len(name)-1
#     for i in range(len(name)):
#         if name[i] != 'A':
#             min_move = min((ord(name[i]) - 65), (91 - ord(name[i])))
#             print(f"{name[i]}:{ord(name[i])}, A-> {ord(name[i]) - 65} , <-A {91 - ord(name[i])} | min : {min_move}")
#             moves += min_move

#         j = i + 1
#         while j < len(name) and name[j] == 'A':
#             j += 1
#         # i까지 갔다가 돌아가고, 남은 문자 끝까지 가는 거리
#         min_move = min(min_move, i + len(name) - j + min(i, len(name) - j))

#     return moves+min_move
