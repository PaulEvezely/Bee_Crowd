x,y,z=input().split()
x,y,z=float(x),float(y),float(z)
if x-y>0:
    if z<x+y and (x-y) < z:
        print(f'Perimetro = {x+y+z}')
    else:
        print(f'Area = {(x+y)/2*z}')
elif x-y<0:
    if z<x+y and (x-y)*-1 < z:
        print(f'Perimetro = {x+y+z}')
    else:
        print(f'Area = {(x+y)/2*z}')
else:
    if z<x+y and (x-y) < z:
        print(f'Perimetro = {x+y+z}')
    else:
        print(f'Area = {(x+y)/2*z}')
    