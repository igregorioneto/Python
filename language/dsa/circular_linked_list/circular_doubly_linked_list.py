class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class CircularDoublyLinkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      new_node.next = self.head
      new_node.prev = self.head
    else:
      tail = self.head.prev
      tail.next = new_node
      new_node.prev = tail
      new_node.next = self.head
      self.head.prev = new_node

  def display(self):
    if not self.head:
      print("Lista vazia")
      return
    current = self.head
    while True:
      print(current.data, end=" <-> ")
      current = current.next
      if current == self.head:
        break
    print("(head)")

if __name__ == "__main__":
  cll = CircularDoublyLinkedList()
  cll.append(10)
  cll.append(20)
  cll.append(30)
  cll.display()