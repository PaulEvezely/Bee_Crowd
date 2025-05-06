lista=[]
lista1=[]
n=int(input())
for i in range(n):
    lista1.append(n-i)
o=lista1[0]
for i in range(n-1):
    o=o*lista1[i+1]
    lista.append(o)
print(lista[-1])