# datas = [10,4,8,5,7,2,9]

def sortList(datas):
    n=len(datas)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if datas[j]>datas[j+1]:
                datas[j],datas[j+1]=datas[j+1],datas[j]
    return datas
    
print(sortList([10,4,8,5,7,2,9]))
