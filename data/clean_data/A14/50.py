# datas = [10,4,8,5,7,2,9]

def sortList(datas):
    for i in range(len(datas)):
        for j in range(1, len(datas) - i):
            if datas[j] < datas[j - 1]:
               # print(f'Swapping {j-1}={datas[j-1]}, {j}={datas[j]}')
                tmp = datas[j]
                datas[j] = datas[j-1]
                datas[j-1] = tmp
                # print(datas)
    return datas
print(sortList([10,4,8,5,7,2,9]))
