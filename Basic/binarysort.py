# 0과 1로 이루어진 배열 오름차순 정렬 

def bin_sort(arr: list[int]) -> None:
    arr[:] = [0] * arr.count(0) + [1] * arr.count(1)
    
def bin_array_sort(arr: list[int]) -> None:
    left, right = 0, len(arr) - 1

    while left < right:
        if arr[left] == 1 and arr[right] == 0:
            arr[left], arr[right] = arr[right],    arr[left]

        if arr[left] == 0:
            left += 1
        if arr[right] == 1:
            right -= 1
            

for arr in ([1, 0, 1, 1, 1, 1, 1, 0, 0, 0], [1, 1]):  
    
    arr1 = arr.copy()
    arr2 = arr.copy()
    arr3 = arr.copy()
    
    print(sorted(arr1))
    bin_sort(arr2)  
    print(arr2)
    bin_array_sort(arr3)
    print(arr3)