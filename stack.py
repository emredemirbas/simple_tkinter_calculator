class Stack:
    def __init__(self):
        self.elements = []

    def get_size(self):
        return len(self.elements)

    def is_empty(self):
        return self.get_size() == 0

    def push(self, item):
        self.elements.append(item)

    def pop(self):
        return self.elements.pop()

    def display(self):
        print(self.elements)

    def remove_all_elements(self):
        self.elements = []
        # while not self.is_empty():
        #     self.pop()
