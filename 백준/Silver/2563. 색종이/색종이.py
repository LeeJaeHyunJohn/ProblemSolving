paper = [[0]*100 for _ in range(100)]
a=[]
n=int(input())
for i in range(n):
  a.append(list(map(int, input().split())))

for coordinate in a:
  for i in range(coordinate[0],coordinate[0]+10):
    for j in range(coordinate[1],coordinate[1]+10):
      paper[j][i]=1


# print(paper.count(1)) 바로 아래 레벨의 원소들만 센다. 즉 paper의 원소는 전부 list이므로 1과 같은 원소는 하나도 없다.
area = sum(sum(row) for row in paper)
print(area)