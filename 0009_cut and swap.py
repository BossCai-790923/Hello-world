'''
Requirement: cut and swap
Requirement 1) create a list which contains 10 int numbers from 1 to 10
Requirement 2) let user to input a 'cut' number: from 1 to 9
Requirement 3) You cut the list in 2 parts at index 'cut', and you swap the 2 parts, print the new list
'''
ql=[]
wl=[]
new_l=[]
c=input('cut number: ')
while c !='exit':
    l=list(range(1,11))
    print(l)
    print('_______________________________')
    int_c=int(c)
    ql=l[0:int_c]
    wl=l[int_c:]
    print(wl)
    print(ql)
    new_l+=wl
    new_l+=ql
    print(new_l)
    wl.clear()
    new_l.clear()
    ql.clear()
    c=input('cut number:')
