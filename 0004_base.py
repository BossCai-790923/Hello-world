x=int(input('convert(10-2):'))
y=bin(x)
pl=list(y)
pl.remove('0')
pl.remove('b')
f=''.join(pl)
print(f)
z=str(input('convert(2-10):'))
d=int(z,2)
print(d)