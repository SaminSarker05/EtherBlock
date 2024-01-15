'''
- a singly linked list class that connects nodes
- optimized for frequent insertions
'''

class Node:
  def __init__(self, data=None):
    self.data = data
    self.next_node = None

  def __str__(self):
    return str(self.data)


class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def append(self, data):
    new_node = Node(data)
    if (self.head is None):
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.new_node = new_node
      self.tail = new_node

  def printList(self):
    cursor = self.head
    print(cursor.next_node)
    while (cursor):
      print(cursor)
      cursor = cursor.next_node
    


chain = LinkedList()
chain.append(1)
chain.append(2)

chain.printList()
