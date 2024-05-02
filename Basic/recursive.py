'''
2 <= '한 테이블에 앉을 수 있는 사람의 수 ' <= 10
'''
import time

n = 100
cnt = 0
def graph(node, last):  # last : 이전화살표에 적힌 숫자(앉는 사람 수)
    # print(f'{node} 명 남음 (node)')
    global cnt
    
    if node == 0 :
        cnt += 1   
        # print('--- cnt 증가 ---')
    
    for i in range(max(2,last), min(node,10)+1):
        # print(f'{i} 명 앉음')     
        # print(f'{" "*(n-node)*2} graph({node-i},{i}) 실행')   
        graph(node-i,i)
    # print(f'{node} 에서 리턴')
    
    return cnt

s = time.time()
print(graph(n,0))
e = time.time()
print(e-s)

'''
 graph(4,2) 실행
     graph(2,2) 실행
         graph(0,2) 실행
--- cnt 증가 ---
     graph(1,3) 실행
     graph(0,4) 실행
--- cnt 증가 ---
 graph(3,3) 실행
       graph(0,3) 실행
--- cnt 증가 ---
 graph(2,4) 실행
 graph(1,5) 실행
 graph(0,6) 실행
--- cnt 증가 ---


6 명 남음 (node)
2 명 앉음

graph(4,2) 실행
4 명 남음 (node)
2 명 앉음

graph(2,2) 실행
2 명 남음 (node)
2 명 앉음

graph(0,2) 실행
0 명 남음 (node)
0 에서 리턴

2 에서 리턴

3 명 앉음

graph(1,3) 실행
1 명 남음 (node)
1 에서 리턴

4 명 앉음

graph(0,4) 실행
0 명 남음 (node)
0 에서 리턴

4 에서 리턴

3 명 앉음

graph(3,3) 실행
3 명 남음 (node)
3 명 앉음

graph(0,3) 실행
0 명 남음 (node)
0 에서 리턴

3 에서 리턴

4 명 앉음

graph(2,4) 실행
2 명 남음 (node)
2 에서 리턴

5 명 앉음

graph(1,5) 실행
1 명 남음 (node)
1 에서 리턴

6 명 앉음

graph(0,6) 실행
0 명 남음 (node)
0 에서 리턴

6 에서 리턴
'''
