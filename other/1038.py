number1,number2=input().split()
number1=int(number1)
number2=int(number2)
list2=[4.00,4.50,5.00,2.00,1.50]
result=list2[number1-1]*number2
print('Total: R$ %0.2f'%result)