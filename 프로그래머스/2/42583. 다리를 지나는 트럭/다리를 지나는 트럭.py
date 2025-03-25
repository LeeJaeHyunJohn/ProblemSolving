from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    time=0
    current_weight=0
    #다리 위 상태 시뮬레이션..0은 비어 있는 공간
    bridge=deque([0]*bridge_length)
    
    while bridge:  
        current_weight-=bridge.popleft()
        time +=1
        
        #truck_weights가 비어있지 않다면
        if truck_weights:
            if current_weight + truck_weights[0] <=weight:
                #굳이 queue로 변환 안 하고 pop(0) 사용
                truck = truck_weights.pop(0)
                bridge.append(truck)
                current_weight +=truck
            else:
                bridge.append(0)
    return time