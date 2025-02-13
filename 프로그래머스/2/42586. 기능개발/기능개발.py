from collections import deque

def solution(progresses, speeds):
    answer = []
    days=deque()
    
    for i in range(len(progresses)):
        d=(100-progresses[i])//speeds[i]
        if (100-progresses[i])%speeds[i]==0:
            days.append(d)
        else:
            days.append(d+1)
            
    while days:
        first=days.popleft()
        count=1
        
        while days and days[0] <=first:#큐가 비거나 뒤의 조건을 만족할때까지
            days.popleft()
            count+=1
            
        answer.append(count)
                                                      
    return answer

# import math

# def solution(progresses, speeds):
#     answer = []
#     rest = []
#     temp = []

#     size = len(progresses)

#     for i in progresses:
#         rest.append(100 - i)

#     for i in range(size):
#         temp.append(math.ceil(rest[i] / speeds[i]))

#     cnt = 0
#     p = temp[0]
#     for i in range(len(temp)):
#         if p < temp[i]:
#             answer.append(cnt)
#             p = temp[i]
#             cnt = 0
#         cnt += 1
#     answer.append(cnt)


#     return answer