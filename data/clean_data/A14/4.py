# datas = [10,4,8,5,7,2,9]

def sortList(datas):
    for i in range(0, len(datas)-1):
        for j in range(i+1, len(datas)):
            if datas[i] > datas[j]:
                temp = datas[j]
                datas[j] = datas[i]
                datas[i] = temp
    return datas

    
print(sortList([10,4,8,5,7,2,9]))
