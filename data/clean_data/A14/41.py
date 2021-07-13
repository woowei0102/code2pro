# datas = [10,4,8,5,7,2,9]

def sortList(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list
print(sortList([10, 4, 8, 5, 7, 2, 9]))



