datas = [10, 4, 8, 5, 7, 2, 9]

def sortList(list):
    for i in range(0, len(list) - 1):  # 有n-1回合(n為數字個數)
        for j in range(0, len(list) - 1 - i):  # 每回合進行比較的範圍
            if list[j] > list[j + 1]:  # 是否需交換
                tmp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = tmp
    return list

print(sortList([10, 4, 8, 5, 7, 2, 9]))