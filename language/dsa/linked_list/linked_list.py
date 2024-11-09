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

  def search(self, data):
    current = self.head
    while current:
      if current.data == data:
        return True
      current = current.next
    return False

  def remove(self, data):
    current = self.head
    previous = None
    while current:
      if current.data == data:
        if previous is None:
          self.head = current.next
        else:
          previous.next = current.next
        return True
      previous = current
      current = current.next
    return False

if __name__ == "__main__":
  linked_list = LinkedList()

  linked_list.append(1)
  linked_list.append(2)
  linked_list.append(3)

  linked_list.display()

  print(linked_list.search(2))
  print(linked_list.search(4))

  linked_list.remove(2)
  linked_list.display()