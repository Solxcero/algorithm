# 제너레이터 표현식 

'''
iterable 
: 반복문 뒤에 넣은 것

iterator 
: iterable 을 만드는 방법 중 하나
: next(iterator) : 내부의 요소를 꺼낼 수 있음

generator 
: iterator 를 만드는 방법 중 하나
'''

gnrt = (
    i * i 
    for i in range(1,100+1)
)

print(next(gnrt)) # 1
print(next(gnrt)) # 4
print(next(gnrt)) # 9


# 제너레이터 함수 
def gen_func():
    for i in range(1,100+1):
        yield i*i
    
gnrt = gen_func()
print(next(gnrt)) # 1


'''
리스트 내포 : 메모리 사용량이 많음
제너레이터 : 메모리 사용량이 적음
'''