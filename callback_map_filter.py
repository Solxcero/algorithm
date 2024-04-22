# 함수를 변수에 저장 , 매개변수로 전달되는 함수 

# 1. 콜백함수 
def call_10_times(callback):
    for i in range(10):
        callback(i)

def print_hello(param):
    print(f'안녕하세요 {param}')
    
call_10_times(print_hello)

# 2. map(), 내포 
def power(num):
    return num**2

A = [1,2,3,4,5]
iterator = map(power,A)
print(list(iterator))

print([num**2 for num in range(1,5+1)])

# 3. fliter(함수,리스트)
def odd(num):
    if num % 2 == 1:
        return True
    else:
        return False
A = [1,2,3,4,5]
iterator = filter(odd,A)
print(list(iterator))

print([num for num in range(1,5+1) if num % 2==1])