y=int(input('Year:'))
m=int(input('Month (1-12):'))
d=int(input('Day (1-31):'))
#list_month
lm=['X',
'January',
'February',
'March',
'April',
'May',
'June',
'July',
'August',
'September',
'October',
'November',
'December']

ld=['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']


print(lm[m],end=' ')
print(d,ld[d-1],sep='',end=' ')
print(y,end=' ')

