def add(a,b):
    plus=0
    var=0
    while plus<=b:
        if plus==0:
            plus=a
        plus=plus+a+1
        var+=1
        a=a+1
    return var + 1

x=int(input())
z=-1000
while x>=z:
    z=int(input())
print(add(x,z))
