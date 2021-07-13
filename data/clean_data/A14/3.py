#datas = [10,4,8,5,7,2,9]
temp = 0

def sortList(datas):
    for passnum in range(len(datas)-1,0,-1):
        for i in range(passnum):
            if datas[i] > datas[i+1]:
                temp = datas[i+1]
                datas[i+1] = datas[i]
                datas[i] = temp
    return datas
    
print(sortList([10,4,8,5,7,2,9]))