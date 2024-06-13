# 이분탐색은 정렬된 배열에서 타겟값을 효율적으로 찾는 알고리즘.~
# 입국심사 문제는 최소시간을 찾는 문제... 그렇다면... 
# 이분 탐색은 배열이 정렬되어 있어야 한다는 전제 조건이 있는데, 여기서 정렬된 배열이 도대체 무엇인가.

# 시간을 오름차순으로 정렬해야한다...

def solution(n, times):
    left, right = 1, max(times)*round(n/len(times))

    while left <= right:
        mid = (left + right) // 2
        tmp = 0

        for t in times:
            tmp += mid//t

        print(f'mid: {mid}, tmp: {tmp}')

        if tmp >= n :
            right = mid -1
        else:
            left = mid +1


    return left  



print(solution(6,[10,7]))