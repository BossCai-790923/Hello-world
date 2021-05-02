
# merge
list_a = [1,5,7,9,13,15,24,27,78,110,167]
list_b = [2,2,6,8,16,17,18,19,99]
# to list_ab


# merge
list_c = [1,5,7]
list_d = [2,2,6,8,16,17,18,19,99]
# to list_cd

# merge
list_e = []
list_f = [2,2,6,8,16,17,18,19,99]
# to list_ef
x=[]
list_ab=[]
list_cd=[]
list_ef=[]
x+=list_a
x+=list_b
for a in range(len(x)):
    index=0
    for b in list_ab:
        if b < x[a]:
            index+=1
        else:
            break
    list_ab.insert(index,x[a])
print(list_ab)
x.clear()
x+=list_c
x+=list_d
for a in range(len(x)):
    index=0
    for b in list_cd:
        if b < x[a]:
            index+=1
        else:
            break
    list_cd.insert(index,x[a])
print(list_cd)
x.clear()
x+=list_e
x+=list_f
for a in range(len(x)):
    index=0
    for b in list_ef:
        if b < x[a]:
            index+=1
        else:
            break
    list_ef.insert(index,x[a])
print(list_ef)
x.clear()


