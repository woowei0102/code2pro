# datas = [10,4,8,5,7,2,9]

def sortList(objs):
    for passnum in range(len(objs)-1, 0, -1):
        for i in range(passnum):
            if objs[i] < objs[i+1]:
                temp = objs[i]
                objs[i] = objs[i+1]
                objs[i+1] = temp
    return objs
    
print(sortList([10,4,8,5,7,2,9]))
