x=0

x=sum(range(0,101))
print(x)
x=list(range(0,101))
print(x)
y=[]
for i in range(101):
    x[i]=str(x[i])
for i in range(101):
    y+=list(x[i])
print(y)
for i in range(101):
    x[i]=int(y[i])
print(x)
n=0
for i in range(101):
    n+=x[i]
print(n)