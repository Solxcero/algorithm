# url : https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=python3
from collections import deque
def solution(bridge_length, weight, truck_weights):
    elapsed_time = 0 # 경과시간
    bridge = deque([0] * bridge_length)  # 다리 위
    bridge_weight = 0  # 다리 위 무게 
    truck_weights = deque(truck_weights)  # 큐 자료형으로 바꿔주기

    while truck_weights or bridge_weight > 0:
        elapsed_time += 1
        
        exiting_truck = bridge.popleft()
        bridge_weight -= exiting_truck
        
        if truck_weights:
            # 다음 트럭이 다리에 올라갈 수 있는지 확인
            if bridge_weight + truck_weights[0] <= weight:
                # 트럭을 다리 위에 올린다.
                entering_truck = truck_weights.popleft()
                bridge.append(entering_truck)
                bridge_weight += entering_truck
            else:
                # 트럭이 올라갈 수 없으면 0을 넣어 공간 유지
                bridge.append(0)
        print(f'bridge: {bridge}')
        print(f'Elapsed Time : {elapsed_time}')

    return elapsed_time

                    
    
                
        
    
print(solution(2,10,[7,4,5,6]))
# print(solution(100,100,[10]))
# print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))


## 다른 풀이
'''
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    count = 0
    Time = 0
    Truck_weight = 0
    truck_move = deque()

    while True:       
        print(f'truck : {truck_weights[count]}')
        # 트럭 다리 올라가는 조건
        if count < len(truck_weights) and weight >= Truck_weight + truck_weights[count]:
            truck_move.append((truck_weights[count], bridge_length + 1 + Time)) # 튜플로 사용 
            Truck_weight += truck_weights[count]
            print(f'1 : {truck_move}')
            count += 1

        # 트럭 다리 다 올라옴
        if count >= len(truck_weights):
            print(f'2 : {truck_move}')
            answer = truck_move[-1][1]
            break

        # 못올라옴
        else:
            Time += 1
            if truck_move and truck_move[0][1] == Time + 1:
                Truck_weight -= truck_move[0][0]
                truck_move.popleft()
                print(f'3 : {truck_move}')
        print()
    
    return answer
'''