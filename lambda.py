'''
def power(num):
    return num**2
'''

power = lambda num : num**2
print(power(10))

'''
def is_odd(num):
    return num % 2 == 1
'''
is_odd = lambda num : num % 2 ==1
print(is_odd(10)) 

# Example
A = [1,2,3,4,5]
res = map(lambda num : num ** 2, A)
print(list(res))

res2 = filter(lambda num : num % 2 == 1, A)
print(list(res2))