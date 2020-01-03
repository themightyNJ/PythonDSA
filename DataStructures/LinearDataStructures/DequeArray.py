'''
Deque also known as Double Ended Queue, is a form of queue that allows insertion and deletion from both front and rear.

Deque Operations/ADT:
    -> insertFront(object) : Adds the element at the first position.
    -> insertRear(object) : Adds the element at the last position.
    -> removeFront() : Deletes the element from the front.
    -> removeRear() : Deletes the element from the rear.
    -> len() : Returns the number of elements present in the deque.
    -> first() : Returns the first element without removing it.
    -> last() : Returns the last element without removing it.
    -> isEmpty() : Checks whether the deque is empty or not.
'''

import sys #For exception handling

class ArrayDeque:
    '''Constructor for the class.'''
    def __init__(self):
        '''Using list to implement queue arrays.'''
        self.data = list()
    def insertFront(self,element):
        '''Adds the element at the first position.'''
        self.data.append(element)
        print("Inserted Successfully!")
    def insertRear(self,element):
        '''Adds the element at the last position.'''
        self.data.insert(0,element)
        print("Inserted Successfully!")
    def removeFront(self):
        '''Deletes the element from the front.'''
        '''If Deque is empty then it raises an exception.'''
        try:
            print("Deleted Successfully!")
            return self.data.pop()
        except IndexError:
            print("Deque size error, Deque is empty!")
    def removeRear(self):
        '''Deletes the element from the rear.'''
        '''If Deque is empty then it raises an exception.'''
        try:
            print("Deleted Successfully!")
            return self.data.pop(0)
        except IndexError:
            print("Deque size error, Deque is empty!")
    def first(self):
        '''Returns the first element without removing it.'''
        '''If Deque is empty then it raises an exception.'''
        try:
            return self.data[-1]
        except IndexError:
            print("Deque size error, Deque is empty!")
    def last(self):
        '''Returns the last element without removing it.'''
        '''If Deque is empty then it raises an exception.'''
        try:
            return self.data[0]
        except IndexError:
            print("Deque size error, Deque is empty!")
    def isEmpty(self):
        '''Checks whether the deque is empty or not.'''
        return len(self.data) == 0

'''Testing the Algo.'''
testDeque = ArrayDeque()
print("Is Deque empty?", testDeque.isEmpty())
testDeque.first()
testDeque.last()
testDeque.removeFront()
testDeque.removeRear()
testDeque.insertFront(10)
testDeque.insertRear(20)
testDeque.insertFront(30)
testDeque.insertRear(40)
print("Deque = ",testDeque.data)
print("Size of Deque = ", len(testDeque.data))
testDeque.removeFront()
testDeque.removeRear()
print("Size of Deque = ", len(testDeque.data))
print("Deque = ",testDeque.data)
