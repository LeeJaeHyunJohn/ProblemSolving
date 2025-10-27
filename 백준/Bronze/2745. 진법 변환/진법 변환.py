N,B=input().split()
B = int(B)
l=[]
sum=0
for w in N:
  if w.isdigit()==True:
    l.append(int(w))
  else:
    val=ord(w)-55
    l.append(val)

x=len(N)
for num in l:
  sum+=(B**(x-1))*int(num)
  x-=1

print(sum)