'''
Stacks are a type of linear data structures and follows a particular order in which the operations are performed.
The order is Last In First Out(LIFO) or First In Last Out(FILO).

Stack Operations/ADT:
    -> push(object) : inserts an element into the Stack.
    -> pop() : removes and returns the top-most/last inserted element of the Stack.
    -> top() : returns the top-most/last inserted element of the Stack without removing it.
    -> len() : returns number of elements present in the Stack.
    -> isEmpty() : checks whether the stack is empty or not.
'''
import sys #For exception handling

class Empty(Exception):
    pass

class ArrayStack:
    '''Constructor for the class.'''
    def __init__(self):
        '''Using list to implement stack arrays.'''
        self.data = list()
    def isEmpty(self):
        '''Checks whether the stack is empty or not.'''
        return len(self.data) == 0
    def push(self, element):
        '''Inserts the element passed as the argument, into the Stack.'''
        self.data.append(element)
    def pop(self):
        '''Removes and returns the last inserted element in the Stack.'''
        '''If the stack is empty then it raises an exception.'''
        try:
            return self.data.pop()
        except IndexError:
            print("Stack size error, Stack is empty.")
    def top(self):
        '''Returns the last inserted element in the Stack without removing it.'''
        '''If the stack is empty then it returns None'''
        try:
            return self.data[-1]
        except IndexError:
            print("Stack is empty.")

'''Testing the algo'''
testStack = ArrayStack()
print("Is Stack empty? : ",testStack.isEmpty())
print("Retrieve the top element : ",testStack.pop())
print("Check the top element : ",testStack.top())
testStack.push(10)
testStack.push(20)
testStack.push(30)
print("Stack = ",testStack.data)
print("Number of elements present in the stack  : ",len(testStack.data))
print("Is Stack empty? : ",testStack.isEmpty())
print("Retrieve the top element : ",testStack.pop())
print("Check the top element : ",testStack.top())
print("Number of elements present in the stack  : ",len(testStack.data))
print("Stack = ",testStack.data)
