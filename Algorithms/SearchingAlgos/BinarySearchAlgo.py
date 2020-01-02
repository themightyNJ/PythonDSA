'''
It works for sorted data only.
Works on Mathematical formula -> mid = ( low + high)/2. PS: The division is integer division.
Where, low is the idex 0, high is the last index of the list and mid is the middle element of the list.
'''

'''Iterable Binary Searching'''
def binarySearch_iter(dataList, key):
    low = 0 #Start of the list
    high = len(dataList)-1 #End of the dataList
    '''When the low becomes larger than the high value, this means the key is not found and the loop condition breaks.'''
    while low <= high:
        mid = (low + high)//2 #Integer division
        if dataList[mid] == key:
            return True
        elif dataList[mid] > key:
            '''If key is smaller than the middle value then the upper half of the list would be neglected'''
            high = mid - 1
        elif dataList[mid] < key:
            '''If key is larger than the middle value then the lower half of the list would be neglected'''
            low = mid + 1
    return False

'''Testing the function'''
testList = [1,2,3,4,5,6,7,8,9]
element1 = 4
element2 = 12
found1 = binarySearch_iter(testList,element1)
found2 = binarySearch_iter(testList,element2)
print("Element ", element1, " is present: ", found1)
print("Element ", element2, " is present: ", found2)

'''Recursive Binary Search'''
def binarySearch_recursive(dataList, key, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if dataList[mid] == key:
            return True
        elif dataList[mid] > key:
            return binarySearch_recursive(dataList, key, low, mid-1)
        elif dataList[mid] < key:
            return binarySearch_recursive(dataList, key, mid+1, high)

'''Testing the function'''
found3 = binarySearch_recursive(testList, element1, 0, len(testList)-1)
found4 = binarySearch_recursive(testList, element2, 0, len(testList)-1)
print("Element ", element1, " is present: ", found3)
print("Element ", element2, " is present: ", found4)
