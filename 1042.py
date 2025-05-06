x,y,z=input().split()
x=int(x)
y=int(y)
z=int(z)

if x<y and x<z:
    print(x)
if y<x and y<z:
    print(y)
if z<x and z<y:
    print(z)
if y < x < z or z < x <y:
    print(x)
if x < y <z or z<y<x:
    print(y)
if y < z < x or x < z < y:
    print(z)
if x>y and x>z:
    print(x)
if y>x and y>z:
    print(y)
if z>y and z>x:
    print(z)
print('')
print(x)
print(y)
print(z)