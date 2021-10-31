# Node class
class Node:
	
	# Function to initialise the node object
	def __init__(self, val):
		self.val = val # Assign data
		self.next = None # Initialize next as null

# Linked List class
class LinkedList:
	def __init__(self):
		self.head = None # Initialize head as None

	# This function inserts a new node at the
	# beginning of the linked list
	def push(self, new_val):
	
		# Create a new Node
		new_node = Node(new_val)

		# Make next of new Node as head
		new_node.next = self.head

		# Move the head to point to new Node
		self.head = new_node

	# This Function checks whether the value
	# x present in the linked list
	def search(self, x):

		# Initialize current to head
		current = self.head

		# loop till current not equal to None
		while current != None:
			if current.val == x:
				return True # data found
			
			current = current.next
		
		return False # Data Not found



# Start with the empty list
llist = LinkedList()

''' Use push() to construct below list
85->2->17->36->78 '''
llist.push(78);
llist.push(36);
llist.push(17);
llist.push(2);
llist.push(85);

if llist.search(85):
  print("True")
else:
  print("False")
