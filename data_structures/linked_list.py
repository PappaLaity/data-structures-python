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
        i = 0
        node = Node(item)
        temp = self.__node
        while i < index and temp.next != None:
            i += 1
            temp = temp.next
        if i == index:
            node.next = temp.next
            temp.next = node
        else:
            print("We can't add at this index the list size is less than the index")

    def insert(self, item):
        node = Node(item)
        if self.__node == None:
            self.__node = node
        else:
            temp = self.__node
            while temp.next != None:
                temp = temp.next
            temp.next = node

    def insertAtEnd(self, item):
        node = Node(item)
        if self.__node == None:
            self.__node = node
        else:
            temp = self.__node
            while temp.next != None:
                temp = temp.next
            temp.next = node

    def delete(self, index):
        previous = None
        temporary = self.__node
        i = 0
        if self.__node == None:
            print("The linked list is empty!")
        elif index == 1:
            temp = self.__node.next
            self.__node = temp
        else:
            # We will for middle and the end of the linked list
            while i < index and temporary.next:
                i += 1
                previous = temporary
                temporary = temporary.next
                # At the end of iteration either i == index or temporary.next == None
            if i == index:
                if temporary.next:
                    # Case of the middle of list
                    previous.next = temporary.next
                    # else:
                    #   # Case end of file
                    #   previous.next = None
            else:
                print(f"Index {index} not in the linked list")

    def display(self):
        node = self.__node
        # node = Node(item)
        while node:
            print(node.data, end="->")
            node = node.next

    def search(self, item):
        temp = self.__node
        i = 0
        while temp.data != item and temp.next:
            temp = temp.next
            i = i + 1
        if temp.data == item:
            print(f"The item {item} is found at position {i}")
            return i
        else:  # Mean the item doest not exist in the list
            print(f"The item {item} doesn't exist in the list")
            return None

    def traverse(self, index):
        i = 0
        temp = self.__node
        # traverse the list
        while i < index and temp.next:
            i += 1
            temp = temp.next
        # Check if we have in the position and the return node/data
        if i == index:
            print(f"The value of node at the {index}th position is {temp.data}")
            return temp
        else:
            print("The index doest exist in the linked list")
            return None

    def get_length(self):
        i = 1
        temp = self.__node
        while temp.next:
            i += 1
            temp = temp.next
        return i

    def access(self, index):
        i, temp = 0, self.__node
        # Get the length of list
        ind = self.get_length()
        #  Check if the index does not exist in the list
        if index < 0 or index > ind:
            print(f"The index {index} doesn't exist in this list")
            return None
        # Traverse the linked list to the index
        while i < index and temp.next:
            i += 1
            temp = temp.next
        # return the data if we are at the index
        if i == index:
            return temp.data

    def update(self, index, new_data):
        i, temp = 0, self.__node
        ind = self.get_length()
        #  Check if the index does not exist in the list
        if index < 0 or index >= ind:
            print(f"The index {index} doesn't exist in this list")
            return None
        # Traverse the list to the index position
        while i < index and temp.next:
            i = i + 1
            temp = temp.next
        # check if we have in index and update data
        if i == index:
            temp.data = new_data
            print("Data successfully updated")
        # if not temp.next:
        #     print(f"The index {ind} don't exist in the list")

    def concatenate(self, new_list):
        temp = self.__node
        while temp.next != None:
            temp = temp.next
        temp.next = new_list
