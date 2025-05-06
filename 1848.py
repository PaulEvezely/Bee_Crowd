def plus(a='0'):
    plu=0
    while True:
        if a=='--*':
            plu+=1
        elif a=='-*-':
            plu+=2
        elif a=='-**':
            plu+=3
        elif a=='*--':
            plu+=4
        elif a=='*-*':
            plu+=5
        elif a=='**-':
            plu+=6
        elif a=='***':
            plu+=7
        else:
            plu==0
        return plu
list=[]
plu=0
while True:
    Eyes=input()
    plu += plus(Eyes)
    if Eyes == 'caw caw':
        list.append(plu)
        plu=0
    if len(list)==3:
        print(list[0])
        print(list[1])
        print(list[2])
        break
