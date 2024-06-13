# 이분탐색은 정렬된 배열에서 타겟값을 효율적으로 찾는 알고리즘.~
# 입국심사 문제는 최소시간을 찾는 문제... 그렇다면... 
# 이분 탐색은 배열이 정렬되어 있어야 한다는 전제 조건이 있는데, 여기서 정렬된 배열이 도대체 무엇인가... times 배열

# 대기인원은 각 심사관별 남은 시간 + 본인 심사 시간 이 최소인 위치로 줄 섬
# 맨 앞의 대기인원이 계산하는 최소 시간이 전체 최소 시간 (각 심사관별 시간은 누적으로 더해야함)

def solution(n,times):
    min_times = 0
    times = sorted(times)
    
    # 첫 순서는 미리 줄 세우기
    for i in range(len(times)):
        times[i] = 

    print(times)
    for _ in range(n):
        if times[0] 
    
    return min_times


def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found



solution(6,[10,7])