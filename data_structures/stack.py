class Stack:
    def __init__(self):
      self.__stack = []

    def push(self,newElement):
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

    def isEmpty(self)->bool:
      return len(self.__stack) == 0
    
    # def isEmptyV2(self)->str:
    #   if len(self.__stack) == 0:
    #     print("The stack is empty")
    #   else:
    #     print("The stack is not empty")

    def size(self):
      return len(self.__stack)

    def display_stack(self):
      print(self.__stack)
