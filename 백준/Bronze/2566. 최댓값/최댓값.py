arr=[]
for i in range(9):
  arr.append(list(map(int, input().split())))
  
max_val=-1
max_i=max_j=0
for i in range(9):
  for j in range(9):
    if arr[i][j] > max_val:
       max_val=arr[i][j]
       max_i,max_j=i,j

print(max_val)
print(max_i+1,max_j+1)