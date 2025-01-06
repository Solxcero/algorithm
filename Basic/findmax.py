import sys
input = sys.stdin.readline

# arr = list(map(int,input().split(', ')))
m1, m2 = 0, 0

def find_max_two(arr: list[int]) -> list[int] :
    if len(arr) < 2:
        return arr
    
    m1, m2 = arr[:2]  # Python 의 Unpacking 기능 (구조 분해 할당)
    '''
    Unpacking 지원X : C, C++, Java, Swift,
    '''
    if m2 > m1 :
        m1, m2 = m2, m1
    for n in arr[2:]:
        if n > m1 : 
            m1, m2 = n, m1  # 동시 할당 (튜플 언패킹킹)
            '''
            오른쪽 값들이 먼저 튜플로 묶여서 저장됨
            동시에 왼쪽 변수들에 할당 
            '''
        elif n > m2 :
            m2 = n
    return [m1, m2]

arr = [[3, -1, 5, 0, 7, 4, 9, 1], [7]]
for a in arr:
    print(find_max_two(a))

# print(find_max_two(arr))