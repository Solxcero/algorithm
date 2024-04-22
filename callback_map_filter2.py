A = [1,2,3,4,5]

# map()
def my_map(callback, lst):
    output = []
    for i in lst:
        output.append(callback(i))
    return output

def power(num):
    return num**2

print(my_map(power,A))

# filter
def my_filter(callback, lst):
    output = []
    for i in lst:
        if callback(i):
            output.append(i)
    return output

def is_odd(num):
    return num % 2 == 1

print(my_filter(is_odd,A))