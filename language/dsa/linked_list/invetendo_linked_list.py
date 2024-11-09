class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node

  def display(self):
    current = self.head
    while current:
      print(current.data, end=" -> ")
      current = current.next
    print("None")

  def reverse(self):
    previous = None
    current = self.head
    next_node = None
    while current:
      next_node = current.next
      current.next = previous
      previous = current
      current = next_node
    self.head = previous

if __name__ == "__main__":
  linked_list = LinkedList()
  linked_list.append(1)
  linked_list.append(2)
  linked_list.append(3)
  linked_list.display()

  linked_list.reverse()
  linked_list.display()