class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, newElement):
        self.__stack.append(newElement)

    def pop(self):
        try:
            self.__stack.pop(-1)
        except:
            print("Something wrong")

    def peek(self):
        try:
            return self.__stack[-1]
        except:
            print("Something wrong")

    def isEmpty(self) -> bool:
        return len(self.__stack) == 0

    def size(self):
        return len(self.__stack)

    # def reverse(self, my_string):
    #     list_string = []
    #     # Create a list of string and integrate to a stack letter by letter
    #     for i in range(len(my_string)):
    #         self.push(my_string[i])
    #     while not self.isEmpty():
    #         # Pop it in list and return it as a string
    #         list_string.append(self.peek())
    #         self.pop()
    #     return "".join(list_string)

    # def are_brackets_balanced(s):
    #     pass

    def display_stack(self):
        print(self.__stack)
