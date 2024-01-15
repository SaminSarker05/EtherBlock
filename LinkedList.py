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
      self.tail.next_node = new_node
      self.tail = new_node

  def printList(self):
    cursor = self.head
    while (cursor):
      print(cursor, end=" -> ")
      cursor = cursor.next_node
    print()
