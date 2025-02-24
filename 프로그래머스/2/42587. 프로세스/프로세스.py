from collections import deque
def solution(priorities, location):
    q = deque([[idx,i] for idx, i in enumerate(priorities)])
    #priorities = [2, 1, 3, 2]
    #[[0, 2], [1, 1], [2, 3], [3, 2]](출력)
    
    #enumerate(priorities)의 결과 : [(0, 2), (1, 1), (2, 3), (3, 2)]
    #deque로 변환된 결과 : deque([[0, 2], [1, 1], [2, 3], [3, 2]])


    cnt = 0
    
    while q:
        now = q.popleft()
        #now=[0,2]
        if any(now[1] < queue[1] for queue in q): 
            #2<1,3,2
            #any는 True가 하나라도 있으면 True를 반환함
            q.append(now)
        else :
            cnt += 1 #출력된 문서 개수 증가
            if now[0] == location : #찾던 location이면 반환
                return cnt 
            
            
            
    