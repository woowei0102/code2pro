# datas = [10,4,8,5,7,2,9]

def sortList(list):
     listLength = len(list)
     i = 0
     while i < listLength-1:
         j = listLength - 1
         while j > i :
             if list[j] < list[j-1]:
                 tempNum = list[j]
                 list[j] = list[j-1]
                 list[j-1] = tempNum

             j = j - 1
         i = i + 1

     return list

    
print(sortList([10,4,8,5,7,2,9]))