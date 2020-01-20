class LINE:

    def __init__(self):
        self.data = []

    def add(self, *arg):
        index = 0
        for i in range(len(arg)):
            self.data.append(arg[index])
            index += 1

    def peek_first_item(self):
        return self.data.pop(0)

    def show_last_item(self):
        return self.data[len(self.data) - 1]

    def show_all_data(self):
        return self.data

myline = LINE()
myline.add(1, 2, '11g', 'Hello world' )
print(myline.show_all_data())
print(myline.peek_first_item())
print(myline.show_all_data())
