class Stack:

    def __init__(self):
        self.data = []

    def add(self, *data):
        index = 0
        for i in range(len(data)):
            self.data.append(data[index])
            index += 1

    def pop(self):
        self.data.pop()

    def peek(self):
        return self.data[len(self.data) - 1]

    def show_data(self):
        print(self.data)

mystack = Stack()
mystack.add('qqq', 1, 2, 4)
mystack.show_data()
a = mystack.peek()
print(a)