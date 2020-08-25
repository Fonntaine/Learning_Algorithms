data = [2, 4, 7, 9, 11, 16, 19, 20, 23, 24, 56, 76, 94]
data2 = [2, 4, 7, 9, 11, 16, 19, 22, 23, 24, 54, 76, 94]
target = 12
def Linear_Search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            print("Your target is in the data base")
    return False

#Linear_Search(data2, 22)  

def Binary_Search(data, target):
    low = 0
    high = len(data)

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
    

def Binary_Search_Recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return Binary_Search_Recursive(data, target, low, mid-1)
        else:
            return Binary_Search_Recursive(data, target, mid+1, high)



print(Binary_Search(data, target))
print(Binary_Search_Recursive(data, target, 0, len(data)-1))

