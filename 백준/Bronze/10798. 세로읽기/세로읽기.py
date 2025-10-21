a=[]

for i in range(5):
  a.append(input())

# 결과를 저장할 빈 문자열
result=''

max_length = max(len(word) for word in a)

for col in range(max_length):
  for row in range(5):
    if len(a[row])>=col+1:
      result+=a[row][col]

print(result)