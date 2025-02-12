
def solution(arr):
    answer = []
    answer.append(arr[0])
    
    i=1
    while i < len(arr):
        if arr[i] !=arr[i-1]:
            answer.append(arr[i])
            
        i+=1
                         
    return answer