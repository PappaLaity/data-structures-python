class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList:

    def __init__(self):
        self.__node = None

    def head(self):
      return self.__node

    def insertAtBeginning(self, item):
        node = Node(item)
        node.next = self.__node
        self.__node = node

    def insertAfter(self, item, index):
        i = 1
        node = Node(item)
        temp = self.__node
        # print(temp.data)
        while i < index and temp.next != None:
          i += 1
          temp = temp.next
        if i == index : 
          node.next = temp.next
          temp.next = node
        else :
          print("we can't add at this index the list size is less than the index")


    def insert(self, item):
      node = Node(item)
      if self.__node == None:
        self.__node = node 
      else:
        temp = self.__node
        while (temp.next != None):
          temp = temp.next
        temp.next = node
    
    def insertAtEnd(self, item):
      node = Node(item)
      if self.__node == None:
        self.__node = node 
      else:
        temp = self.__node
        while (temp.next != None):
          temp = temp.next
        temp.next = node

    def deleteItem(self,index):
      previous = None
      temporary = self.__node
      i = 1
      if index == 1 : 
        temp = self.__node.next
        self.__node = temp
      else:
        # We will for middle and the end of the linked list
        while i<index and temporary.next:
          i += 1
          previous = temporary
          temporary = temporary.next
        # At the end of iteration either i == index or temporary.next == None
        if i == index:
          if temporary.next :
            # Case of the middle of list
            previous.next = temporary.next
          # else:
          #   # Case end of file
          #   previous.next = None
        else :
          print(f"Index {index} not in the linked list")


    def display(self):
        node = self.__node
        # node = Node(item)
        while node:
          print(node.data, end = "->")
          node = node.next

    def search(self, item):
        pass

    def traverse(self,index):
       pass

    def get_length(self):
        pass

    def access(self, index):
        pass

    def update(self, index, new_data):
        pass
    
    def concatenate(self, new_list):
      temp = self.__node
      while (temp.next != None):
        temp = temp.next
      temp.next = new_list