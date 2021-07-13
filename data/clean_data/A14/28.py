# datas = [10,4,8,5,7,2,9]

def sortList(datas):
    for i in range(0,len(datas)-1):
        flag = False
        for j in range(0,len(datas)-1-i):
            if datas[j] > datas[j+1]:
                flag = True
                temp = datas[j]
                datas[j] = datas[j+1]
                datas[j+1] = temp
        if flag == False:
            break
    return datas
    
print(sortList([10,4,8,5,7,2,9]))
