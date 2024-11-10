class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      return
    current = self.head
    while current.next:
      current = current.next
    current.next = new_node
    new_node.prev = current

  def display(self):
    current = self.head
    while current:
      print(current.data, end=" <-> ")
      current = current.next
    print("None")

  def remove_duplicates(self):
    current = self.head
    seen = set()
    while current:
      if current.data in seen:
        if current.prev:
          current.prev.next = current.next
        if current.next:
          current.next.prev = current.prev
        if current == self.head:
          self.head = current.next
      else:
        seen.add(current.data)
      current = current.next

if __name__ == "__main__":
  dll = DoublyLinkedList()
  dll.append(4)
  dll.append(2)
  dll.append(4)
  dll.append(3)
  dll.append(2)
  dll.append(5)
  dll.display()
  dll.remove_duplicates()
  dll.display()