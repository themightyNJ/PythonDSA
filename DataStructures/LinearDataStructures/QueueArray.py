'''
Queues are a type of linear data structures and follows a particular order in which the operations are performed.
The order is First In First Out(FIFO) or Last In Last Out(LILO).

Queue Operations/ADT:
    -> enqueue(object) : The elements are inserted from the rear of the queue.
    -> dequeue() : The element will remove and return from the front of the queue.
    -> first() : returns the element from the front of the queue without removing it.
    -> len() : returns the number of elements present in the queue.
    -> isEmpty() : checks whether the queue is empty or not.
'''

import sys #For exception handling

class ArrayQueue:
    '''Constructor for the class.'''
    def __init__(self):
        '''Using list to implement queue arrays.'''
        self.data = list()
    def isEmpty(self):
        '''Checks whether the queue is empty or not.'''
        return len(self.data) == 0
    def enqueue(self, element):
        '''The element will inserted at the rear of the queue.'''
        print("Inserted successfully!")
        self.data.insert(0,element)
    def dequeue(self):
        '''The first element will be removed and returned from the front of the queue.'''
        '''If the queue is empty then it raises an exception.'''
        try:
            print("Dequeued successfully!")
            return self.data.pop()
        except IndexError:
            print("Queue size error, Queue is empty!")
    def first(self):
        '''Will return the element from the front of the queue without removing it.'''
        '''If the queue is empty then it raises an exception.'''
        try:
            return self.data[-1]
        except IndexError:
            print("Queue size error, Queue is empty!")

'''Testing of algo'''
testQueue = ArrayQueue()
print("Number of elements : ",len(testQueue.data))
print("First element : ",testQueue.first())
print("Queue = ",testQueue.data)
testQueue.dequeue()
testQueue.enqueue(10)
testQueue.enqueue(20)
testQueue.enqueue(30)
print("Queue = ",testQueue.data)
print("Number of elements : ",len(testQueue.data))
print("First element : ",testQueue.first())
testQueue.dequeue()
print("Number of elements : ",len(testQueue.data))
testQueue.enqueue(40)
print("Queue = ",testQueue.data)
print("Number of elements : ",len(testQueue.data))
print("First element : ",testQueue.first())
