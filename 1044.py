n1,n2 = map(int,input().split())
if n1 > n2:
    if n1%n2==0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
if  n2 > n1:
    if n2 % n1==0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')