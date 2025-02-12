#11047
n,k=map(int, input().split())

money=[]

for i in range(n):
  money.append(int(input()))

money=list(reversed(money))

count=0
for coin in money:
  count+=k//coin
  k%=coin

print(count)