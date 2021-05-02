x = int(input('how_many_Decimal:'))
min_3_pi = 3
class_variable_1=2
class_variable_2=3
class_variable_3=4

x=int(x)
for i in range(x):
    min_3_pi+=(4/(class_variable_1*class_variable_2*class_variable_3))
    class_variable_1+=2
    class_variable_2+=2
    class_variable_3+=2
    min_3_pi-=(4/(class_variable_1*class_variable_2*class_variable_3))
    class_variable_1 += 2
    class_variable_2 += 2
    class_variable_3 += 2
pi=min_3_pi
print(pi)