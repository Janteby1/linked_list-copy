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

	def search_rec (self, n, data):
		# n = self.head
		if n.data == data:
			return True
		else:
			return self.search_rec(n.next, data)
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
		n = self.head
		while n != None:
			print(n.data)
			n = n.next
	
	def print_back(self):
		n = self.head
		my_ll_back = []
		while n.next != None:
			my_ll_back.insert(0, n.data)
			n = n.next
		my_ll_back.insert(0, n.data)
		print (my_ll_back)



my_ll = LinkedList(Node("A"))
#b.Node = Node('B')
my_ll.append("B")
my_ll.append('D')
my_ll.insert('C', 2)
print (my_ll.search_rec(my_ll.head, 'C'))
# print (my_ll.delete('C'))
# my_ll.print_ll()
my_ll.print_back()
# print (my_ll.head.next.next.data)
# print (my_ll)
# print (LinkedList)