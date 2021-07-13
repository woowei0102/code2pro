# datas = [10,4,8,5,7,2,9]

def sortList(datas):
    for i in range(len(datas)):
        for j in range(len(datas)-1):
            if datas[j]>datas[j+1]:
                datas[j],datas[j+1]=datas[j+1],datas[j]
    return datas
    
print(sortList([10,4,8,5,7,2,9]))
