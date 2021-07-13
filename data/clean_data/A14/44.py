# datas = [10,4,8,5,7,2,9]

def sortList(datas):
    for i in range(0, len(datas)-1):
        for j in range(0, len(datas)-1-i):
            if datas[j] > datas[j+1]:
                tmp = datas[j]
                datas[j] = datas[j+1]
                datas[j+1] = tmp
    return datas

    
print(sortList([10,4,8,5,7,2,9]))
