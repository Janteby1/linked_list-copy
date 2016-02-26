class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self, head):
		self.head = head

	def append (self, data):
		new = Node(data)
		n = self.head
		while n.next != None:
			n = n.next
		n.next = new

	def insert(self, data, index):
		n = self.head
		new = Node(data)
		counter = 0

		while n.next != None:
			if counter == index - 1:
				new.next = n.next
				n.next = new
			counter += 1
			n = n.next

	def search (self, data):
		n = self.head
		while n.next != None:
			if n.data == data:
				return True
			else:
				n = n.next
		return False

	def search_recersive (self, n, data):
		# n = self.head
		if n.data == data:
			return True
		else:
			return self.search_recersive(n.next, data)
		return False

	def delete (self, data):
		n = self.head
		while n.next != None:
			if n.next.data == data:
				n.next = n.next.next
				return True
			else:
				n = n.next
		return False

	def print_ll(self):
		# n = self.head
		for n in self:
			print(n.data)


	def __iter__(self):
		node = self.head
		while node:
			yield node
			node = node.next

	def __repr__(self):
		return str(self)

	def __str__(self):
		return '-->'.join(n.data for n in self)

my_ll = LinkedList(Node("A"))
my_ll.append("B")
my_ll.append('D')
my_ll.insert('C', 2)

print (my_ll.search_rec(my_ll.head, 'C'))
my_ll.print_ll()

