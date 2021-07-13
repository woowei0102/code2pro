# datas = [10,4,8,5,7,2,9]

def sortList(datas):
    for i in range(len(datas)-1):
        for j in range (len(datas)-1-i):
            if(datas[j]>datas[j+1]):
                temp = datas[j]
                datas[j] = datas[j+1]
                datas[j+1] = temp
    return datas

    
print(sortList([10,4,8,5,7,2,9]))
