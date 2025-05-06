tear= int(input())
points=0
lista=[]

attempt = input().split()
attempt_true=attempt[:5]
for j in range(0,5):
    lista.append(int(attempt_true[j]))
for i in range(0,5):
    if lista[i] == tear:
        points+=1
print(points)