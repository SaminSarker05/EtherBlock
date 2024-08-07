'''
A singly linked list class that connects nodes
and is optimized for frequent insertions
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
    self.n = 0
  
  def __len__(self):
    return self.n
  
  def append(self, data):
    new_node = Node(data)
    if (self.head is None):
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next_node = new_node
      self.tail = new_node
    self.n += 1

  def printList(self):
    cursor = self.head
    while (cursor):
      print(cursor.data, end=" -> ")
      cursor = cursor.next_node

  def last(self):
    return self.tail

  def __iter__(self):
    cursor = self.head
    while cursor:
      yield cursor
      cursor = cursor.next_node
