'''
Created on 01.04.2018

@author: Stefan Schneider
Github: stefschneider1970

based on the code of:
Vincent Russo
https://github.com/vprusso/youtube_tutorials/tree/master/data_structures/trees/binary_trees
'''
class Queue(object):
    '''
    a class for a queue
    '''

    def __init__(self) -> list:
        '''
        Creates an empty queue. Type: List
        '''

        self.items = []


    def is_empty(self) -> bool:
        '''
        Checks whether queue is empty.
        :return: True (queue is empty) or False (queue is not empty)
        '''

        return self.items == []


    def enqueue(self, item):
        '''
        Inserts an item at the end of queue.
        :param item: item to insert
        '''

        self.items.insert(0, item)


    def dequeue(self):
        '''
        Deletes item at the beginning of queue.
        '''

        return self.items.pop()
    
    
    def size(self) -> int:
        '''
        Returns length of queue.
        :param self:
        :return: Length oy queue: Typ: Integer
        '''

        return len(self.items)
    
    
    def peek(self):
        '''
        Returns first item if queue is not empty
        '''

        if not self.is_empty():
            return self.items[-1]
        else:
            raise Exception('Queue is empty.')

'''
TEST
        
queue = Queue()
queue.enqueue(10)
queue.enqueue(6)
queue.enqueue(1)
print(queue.items)
print(queue.size())
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
'''

