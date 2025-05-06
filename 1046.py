x,y=input().split()
if int(x)>int(y) or int(x)==int(y):
    print (f'O JOGO DUROU {(24-int(x))+int(y)} HORA(S)')
else:
    print (f'O JOGO DUROU {(int(x)-int(y))*-1} HORA(S)')