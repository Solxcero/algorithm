
def find_sub_array(arr: list[int], s: int) -> list[int]:
    
    left = 0
    sum = 0
    
    for right in range(left,len(arr)):
            
        while True:
            sum += arr[right]
            right += 1
        

# Test code
sample1 = ([1, 2, 3, 7, 5], 12)
sample2 = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15)
for arr, s in (sample1, sample2):
    print(find_sub_array(arr, s))