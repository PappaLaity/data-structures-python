class Queue:

  __size = 100

  def __init__(self) -> None:
     self.__queue  = []

  def enqueue(self,newElement)-> None:
    if self.isFull():
      print("The queue is full can't add a new element")
    else:
      self.__queue.append(newElement)
      print(f"{newElement} added successfully to the queue\n")


  def dequeue(self)->str:
    if self.isNull():
      return "The queue is Empty!"
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
    else:
      return self.__queue[-1]

  def isFull(self):
    if len(self.__queue) == self.__class__.__size:
      return True
    return False

  def isEmpty(self)->bool:
    if len(self.__queue) == 0:
      return True
    return False

  def display_queue(self):
        print(self.__queue)