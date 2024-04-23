'''
2 <= '한 테이블에 앉을 수 있는 사람의 수 ' <= 10
https://www.youtube.com/watch?v=75nOPZ888sc&list=PLBXuLgInP-5n2fvfXHU9mHVuWBgAKpHNi&index=69
'''
n = 6
cnt = 0
def graph(node, last):
    print(f'{node} 명 남음 (node)')
    
    if node == 0 :
        global cnt
        cnt += 1   
    
    for i in range(max(2,last), min(node,10)+1):
        print(f'{i} 명 앉음')     
        print(f'\ngraph({node-i},{i}) 실행')   
        graph(node-i,i)
    print(f'{node} 에서 리턴\n')
    
    return cnt

print(graph(n,0))

'''
6 명 남음 (node)
2 명 앉음
4 명 남음 (node)
2 명 앉음
2 명 남음 (node)
2 명 앉음
0 명 남음 (node)
0 에서 리턴
2 에서 리턴
3 명 앉음
1 명 남음 (node)
1 에서 리턴
4 명 앉음
0 명 남음 (node)
0 에서 리턴
4 에서 리턴
3 명 앉음
3 명 남음 (node)
3 명 앉음
0 명 남음 (node)
0 에서 리턴
3 에서 리턴
4 명 앉음
2 명 남음 (node)
2 에서 리턴
5 명 앉음
1 명 남음 (node)
1 에서 리턴
6 명 앉음
0 명 남음 (node)
0 에서 리턴
6 에서 리턴
'''
