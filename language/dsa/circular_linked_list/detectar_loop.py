class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class CircularLinkedList:
  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      new_node.next = self.head
    else:
      current = self.head
      while current.next != self.head:
        current = current.next
      current.next = new_node
      new_node.next = self.head

  def display(self):
    if not self.head:
      print("Lista vazia")
      return
    current = self.head
    while True:
      print(current.data, end=" -> ")
      current = current.next
      if current == self.head:
        break
    print("(head)")

  def has_loop(self):
    if not self.head or self.head.next == self.head:
      return True

    slow = self.head
    fast = self.head

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

      if slow == fast:
        return True

    return False

if __name__ == "__main__":
  cll = CircularLinkedList()
  cll.append(10)
  cll.append(20)
  cll.append(30)
  cll.display()
  if cll.has_loop():
    print("Lista é circular")
  else:
    print("Lista não circular")
