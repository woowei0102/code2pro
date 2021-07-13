# datas = [10,4,8,5,7,2,9]

def sortList(datas):
    for i in range(len(datas)-1, -1, -1):
        for j in range(i):
            if datas[j+1]<datas[j]:
                datas[j+1], datas[j] = datas[j],  datas[j+1]
    return datas
    
print(sortList([10,4,8,5,7,2,9]))
