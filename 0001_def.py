nm=float(input('who do you want to know SQRT?'))
def sqrt(x):
    diff = 0.0000000000000000000001
    a=1
    b = x / a
    actual_diff = b - a
    print(f'a:{a},b:{b}.actual diff:{actual_diff}')
    while actual_diff > diff:
        a = (a+b)/2
        b = x/a

        actual_diff = abs(a-b)
        print(f'a:{a},b:{b}.actual diff:{actual_diff}')

    print(f'square root of {x} is {a}')
    print(f'I want to know {nm} "s SQRT {a} * {a} = {a ** 2}')
print(sqrt(nm))
print('Finish')
