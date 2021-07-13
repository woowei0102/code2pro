# datas = [10,4,8,5,7,2,9]

def sortList(datas):
    for i in range(len(datas) - 1):
        for j in range(i, len(datas)):
            if datas[i] > datas[j]:
                datas[i], datas[j] = datas[j], datas[i]
    return datas

print(sortList([10,4,8,5,7,2,9]))