T=int(input())
money=[25,10,5,1]
p=[]
for i in range(T):
  p.append(int(input()))


for m in p:
  count=0
  for k in money:
    count=m//k
    m=m%k
    # print(count)
    # print(m)
    print(count,end=' ')
  print() # 띄어쓰기 