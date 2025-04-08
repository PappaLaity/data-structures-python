class Queue:

    def __init__(self) -> None:
        self.__queue = []

    def enqueue(self, newElement) -> None:
        self.__queue.append(newElement)
        print(f"{newElement} added successfully to the queue\n")

    def dequeue(self) -> str:
        if self.isNull():
            print("The queue is Empty!")
            return None
        else:
            self.__queue.pop(0)
            return "Successfully popped\n"

    def peek(self):
        if self.isNull():
            print("The queue is Empty!")
        else:
            return self.__queue[0]

    def rear(self):
        if self.isNull():
            print("The queue is Empty!")
            return None
        else:
            return self.__queue[-1]

    def isNull(self) -> bool:
        if len(self.__queue) == 0:
            return True
        return False

    def isEmpty(self) -> bool:
        if len(self.__queue) == 0:
            return True
        return False

    def dequeue_asc(self):
      pass

    def display_queue(self):
        print(self.__queue)
