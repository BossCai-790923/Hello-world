x = int(input('how_many_Decimal:'))
class_add = 1
pi = 0



x=int(x)
for i in range(x):
    pi+=(4/class_add)
    class_add+=2
    pi-=(4/class_add)
    class_add+=2
print(pi)

