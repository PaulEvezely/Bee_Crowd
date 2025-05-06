def result(n1,n2):
    solve=(n1+n2)/2
    solve2='%0.2f'% solve
    return solve2
nota_val=0
values=[]
while nota_val<2:
    nota=float(input())
    if 0 <= nota <= 10 :
        values.append(nota)
        nota_val=nota_val+1
    else:
        print('nota invalida')
    if len(values)==2 :
        print(f'media = {result(values[0],values[1])}')
        breakpoint