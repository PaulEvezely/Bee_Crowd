x = float(input())

fibo = ((1+(5**0.5))/2)**x
fibo_less = ((1-(5**0.5))/2)**x
result_fibo = (fibo - fibo_less) / 5**0.5

print('%0.1f' % result_fibo)