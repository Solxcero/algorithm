# recursive 에 memoization 추가
import time
n = 100

memo = {
   
    #키 : 값
    #함수의 매개변수 : 리턴값
   
    
}

def graph(node, last):
    # tuple : immutable -> 딕셔너리 키로 사용 가능
    # memo[(node,last)]
    
    if (node,last) in memo :
        return memo[(node,last)]
    
    # 일반적인 상황
    res = 0
    if node == 0 :
        res += 1
    else:
        for i in range(max(2,last), min(node,10)+1):
            res += graph(node-i,i)
    
    memo[(node,last)] = res
    # print(memo)
    
    return res
s = time.time()
print(graph(n,0))
e = time.time()
print(e-s)
        
        