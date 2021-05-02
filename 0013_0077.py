while True:
    vow=list('aeiou')
    word=input('search vowels:')
    find=[]
    for letter in word:
        if letter in vow:

            find.append(letter)
            letter_index=vow.index(letter)
            vow.pop(letter_index)
            print(vow)
    for vow in find:
        print(find,end='\n')