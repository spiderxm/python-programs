# Some simple functions for Linked List
'''
Made by: Ansh Gupta(@ansh422)
Date: 11/10/2021
'''

# Class for a Node of LinkedList
class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None

# Insert an element at begin that returns head of LinkedList
# Time Complexity: O(1)
def insertAtBegin(head,val):
    if head is None:
      return Node(val)
    tmp=Node(val)
    tmp.next=head
    return tmp

# Insert an element at end of LinkedList and return head
# Time Complexity: O(n)
def insertAtEnd(head,val):
    if head is None:
      return Node(val)
    cur=head
    while cur.next:
        cur=cur.next
    cur.next=Node(val)
    
    return head


# Display all elements in LinkedList
# Time Complexity: O(n)
def display(head):
    cur=head
    while cur:
        print(cur.val)
        cur=cur.next

# Delete all occurrences of an element in LinkedList
# Time Complexity: O(n)
def delete(head,val):
    cur=head
    pre=None
    while cur:
        if cur.val == val:
            if pre is None:
                head=cur.next
            else:
                pre.next=cur.next
        else:
            pre=cur
        
        cur=cur.next
    
    return head
    


