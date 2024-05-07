number = int(input("int : "))
# raise : 사용자에게 오류를 전달함으로써 잘못 사용하고 있음을 알림


if number > 0 :
    print('Positive')
elif number == 0:
    raise NotImplementedError("Not implemented yet")
else:
    raise NotImplementedError("Not implemented yet")