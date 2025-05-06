def bigger(times):

    numbers=[]
    result=[]
    index=[]
    for i in range(times): 
        number=float(input())
        numbers.append(number)
        if numbers[i]==max(numbers):
            result.append(numbers[i])
            index.append(i)
    print(int(max(result)))
    print(index[-1]+1)

bigger(100)
