'''
Creating a linearsearch which has two arguments;
dataList is the list in which we are searching,
key is the data we are searching.
'''
def linearsearch(dataList,key):
    '''position will be used to traverse the loop from the start to the end of the list.'''
    position = 0
    '''flag will used to check whether we have found the key or not.'''
    flag = False
    '''
    Traversing through loop from position 0 to the end of the list.
    Unless the key is not found, the flag would be set to False hence, (not flag) will return True;
    As soon as the key is found, the flag will be set to True hence, (not flag) will return False and loop will break.
    '''
    while position < len(dataList) and not flag:
        '''If key mathches to a data element in the list then it sets the flag to True else increments the loop.'''
        if dataList[position] == key:
            flag = True
        else:
            position += 1
    return flag

'''Testing the function'''
testList = [22,13,45,78,95,73,87,52,30]
element1 = 95
element2 = 99
'''Finding an key the list'''
found1 = linearsearch(testList,element1)
print("Element ", element1, " is present: ", found1)
found2 = linearsearch(testList,element2)
print("Element ", element2, " is present: ", found2)
