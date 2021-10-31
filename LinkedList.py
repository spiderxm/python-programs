#Python program for traversal of a linked list

class Node:
  
	def __init__(self, val):
		self.val = val # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# This function prints contents of linked list
	# starting from head
	def printList(self):
		temp = self.head
		while (temp):
			print (temp.val)
			temp = temp.next



llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)

llist.head.next = second; # Link first node with second
second.next = third; # Link second node with the third node

llist.printList()
