times=int(input())
result=[]
while times > 0:
    r1,r2 = input().split()
    result.append(int(r1)+int(r2))
    times-=1
for i in range(len(result)):
    print(result[i])