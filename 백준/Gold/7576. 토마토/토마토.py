#7576(BFS-토마토)
from collections import deque

m,n = map(int, input().split())

g=[]
for i in range(n):
  g.append(list(map(int, input().split())))

#모든 익은 토마토를 큐에 추가하기
q=deque()

for i in range(n):
  for j in range(m):
    if g[i][j]==1:
      q.append((i,j))


#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():#굳이 bfs(x,y)에서 x,y를 인자로 받을 필요가 없다. 이미 q에 저장.
  while q:
    x,y=q.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<n and 0<=ny<m and g[nx][ny] == 0:
        g[nx][ny]=g[x][y]+1
        q.append((nx,ny))

if q: #큐가 비어있지 않을 때만 bfs를 실행해줘야 함.
  bfs()
#bfs(q[0][0],q[0][1]) 처음에 이렇게 오류를 범함

max_list=[]

for row in g:
  if 0 in row:
    print(-1)
    exit() #프로그램 즉시 종료(처음에 break로 했음)
  else :
    max_list.append(max(row))

#최소 일수 출력(처음이 1로 시작함)
print(max(max_list)-1)