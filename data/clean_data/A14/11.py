def sortList(data):
    for i in range(len(data)-1):
        for j in range(len(data)-1-i):
            if(data[j]>data[j+1]):
                temp=data[j]
                data[j]=data[j+1]
                data[j+1]=temp
    return data
print(sortList([10,4,8,5,7,2,9]))