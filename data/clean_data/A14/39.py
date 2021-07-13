# datas = [10,4,8,5,7,2,9]

def sortList(datas):
    leng=len(datas)
    for i in range(leng):
        for j in range(leng-i-1):
            if datas[j]>datas[j+1]:
                temp=datas[j]
                datas[j]=datas[j+1]
                datas[j+1]=temp
    return datas
    
print(sortList([10,4,8,5,7,2,9]))
