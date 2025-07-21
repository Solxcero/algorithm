price = int(input())

# 500엔, 100엔, 50엔, 10엔, 5엔, 1엔

m = 1000-price
cnt = 0

lst = [500, 100, 50, 10, 5, 1]

for n in lst :
    if m//n >=1 : # 이 조건은 필요가 없군 
        cnt += m//n
        m -= n*(m//n)
    else:
        continue

print(cnt)


# 다른 풀이
# n = 1000 - int(input())
# k = [500, 100, 50, 10, 5, 1]
# c = 0
# for i in k:
#     c += n // i
#     n %= i
# print(c)