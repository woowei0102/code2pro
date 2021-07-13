# datas = [10,4,8,5,7,2,9]

def sortList(datas):
    for i in range(0,len(datas)-1): #有n-1回合(n為數字個數)
        for j in range(0,len(datas)-1-i): #每回合進行比較的範圍
            if datas[j] > datas[j+1]: #是否需交換
                tmp = datas[j]
                datas[j] = datas[j+1]
                datas[j+1] = tmp

    
print(sortList([10,4,8,5,7,2,9]))
