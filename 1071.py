number1= int (input())
number2= int( input())
impares=0
if number1>number2:
    for i in range(number2+1,number1):
        if i%2!=0:
            impares = impares +i
else:
    for i in range(number1+1,number2):
        if i%2!=0:
            impares = impares + i
print(impares)