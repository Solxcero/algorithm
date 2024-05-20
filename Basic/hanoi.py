# 하노이탑  2**n - 1
'''
시작기둥 : A
대상기둥 : B
중간기둥 : C

'''
cnt = 0

def hanoi(num, start, end, sub):
    global cnt
    if num == 1 :
        # print(f'{start} -> {end}')
        cnt += 1
        
    else:
        hanoi(num-1, start, sub, end)
        # print(f'{start} -> {end}')
        cnt += 1
        hanoi(num-1, sub, end, start)
        
nums = int(input("원판 개수 입력 :  "))
hanoi(nums, "A", "B", "C")
print(cnt)
print((2**nums) -1 )