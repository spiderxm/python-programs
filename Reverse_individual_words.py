class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def get_list(self):
        return self.items

def reverse(string):
    S = Stack()
    P = Stack()
    for i in string:
        if i == ' ':
            while not S.isEmpty():
                P.push(S.pop())
            P.push(' ')

        else:
            S.push(i)

    while not S.isEmpty():
        P.push(S.pop())
        
    for j in P.get_list():
        print(j, end='')

reverse('Geeks for Geeks')
