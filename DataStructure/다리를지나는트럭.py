# url : https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=python3
def solution(bridge_length, weight, truck_weights):
    from collections import deque
    # truck_weights.insert(0,truck)
    on_bridge = deque([0]*bridge_length)
    timepast = 0
    weight_sum = 0
    
    while len(truck_weights) != 0:
        weight_sum += truck_weights[0]
        print(f'truck : {truck_weights[0]} , weight : {weight_sum}')
        
        if weight_sum <= weight:
            on_bridge[0] = truck_weights[0]
            print(f'bridge : {on_bridge}')
            timepast += 1
            del truck_weights[0]
            on_bridge.rotate()
            timepast += 1
            
        
        else:
            # weight_sum -= truck_weights[0]
            while weight_sum > weight:
                if on_bridge[-1] == 0:
                    on_bridge.rotate()
                    timepast += 1
                    on_bridge[0] = truck_weights[0]
                    print(f'bridge : {on_bridge}')
                        
                else:
                    weight_sum -= on_bridge[-1]
                    on_bridge[-1] = 0
                    on_bridge.rotate
                    timepast += 1
                    on_bridge[0] = truck_weights[0]
                    print(f'bridge : {on_bridge}')
                    
    
                
        
        
    
    return timepast


solution(2,10,[7,4,5,6])
