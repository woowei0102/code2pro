# datas = [10,4,8,5,7,2,9]

def sortList(datas):
    c=len(datas)
    for i in range(c):
        for j in range(c-i-1):
            if(datas[j]>datas[j+1]):
                datas[j],datas[j+1]=datas[j+1],datas[j]
    return datas
    
print(sortList([10,4,8,5,7,2,9]))
