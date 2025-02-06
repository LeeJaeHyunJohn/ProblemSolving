#1926(BFS)
from collections import deque

n,m = map(int, input().split())
graph=[]

for i in range(n):
  graph.append(list(map(int, input().split())))

#상,하,좌,우 정의
dx=[-1,1,0,0]
dy=[0,0,-1,1]

width_list=[]

def bfs_width(x,y):
  width=0
  queue=deque()
  queue.append((x,y))
  graph[x][y]=0
  while queue:
    x,y=queue.popleft()#이 부분 실수함
    width+=1
    
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      #도화지 벗어난 경우
      if nx<0 or ny<0 or nx>=n or ny>=m :
        continue 
      if graph[nx][ny]==0:
        continue
      if graph[nx][ny]==1:
        graph[nx][ny]=0#실수함
        queue.append((nx,ny))
        

  width_list.append(width)
    
count=0
for i in range(n):
  for j in range(m):
    if graph[i][j]==1:
      bfs_width(i,j)
      count+=1

print(count)
if(count==0):
  print(0)
else:
  print(max(width_list))