import time

# fibonacci
def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
s = time.time()  
print(fibo(40))
e = time.time()
print(f'runtime : {e-s}')
'''
102334155
runtime : 10.090151071548462
'''

# memoization
memo = {1:1, 2:1}
def mm(n):
    if n in memo:
        return memo[n]
    else:
        temp = mm(n-1) + mm(n-2)
        memo[n] = temp
        return temp

ss = time.time()
print(mm(40))
ee = time.time()
print(f'runtime : {ee-ss}')
'''
102334155
runtime : 0.0
'''