def sortList(datas):
    for j in range (len(datas)-1):
        for i in range (len(datas)-1-j):
            if datas[i]>datas[i+1]:
                temp=datas[i]
                datas[i]=datas[i+1]
                datas[i+1]=temp
    return datas
                
print(sortList([10,4,8,5,7,2,9]))
