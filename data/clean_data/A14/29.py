# datas = [10,4,8,5,7,2,9]

def sortList(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

    
print(sortList([10,4,8,5,7,2,9]))
