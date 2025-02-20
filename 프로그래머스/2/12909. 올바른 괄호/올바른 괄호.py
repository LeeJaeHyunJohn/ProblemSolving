def solution(s):
    l = []
    for char in s:
        if char == '(':
            l.append(char)  # 스택에 추가
        else:  # char == ')'
            if not l:  # 스택이 비어 있으면 잘못된 괄호
                return False
            l.pop()  # 스택에서 '(' 제거

    return len(l) == 0  # 스택이 비어 있어야 올바른 괄호
#마지막 부분이 비교 연산이기에 len(l)이 0이면 자동으로 True를 반환하고 아니라면 False를 반환하게 된다. 
    #아래 코드와 같은 역할을 한다.
    
    # if len(l) == 0:
    #     return True
    # else:
    #     return False
