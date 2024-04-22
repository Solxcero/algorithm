'''
2 <= '한 테이블에 앉을 수 있는 사람의 수 ' <= 10
https://www.youtube.com/watch?v=75nOPZ888sc&list=PLBXuLgInP-5n2fvfXHU9mHVuWBgAKpHNi&index=69
'''
n = 6
cnt = 0
def graph(node, last):
    print(f'{node} 노드에 진입')
    if node == 0 :
        global cnt
        cnt += 1   
    
    for i in range(max(2,last), min(node,10)+1):
        print(f'{i} 명 앉음')        
        graph(node-i,i)
    print(f'{node} 에서 리턴')
    
    return cnt

print(graph(n,0))


