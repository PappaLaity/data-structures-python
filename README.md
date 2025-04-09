# Laity Data Structure

A data structure is a way of organizing and storing data in our machine so that it can be accessed and used efficiently. It refers to the logical or mathematical representation of data, as well as the implementation in a computer program.

Data structures can be classified into two broad categories:

*   **Linear Data Structure**: A data structure in which data elements are arranged sequentially or linearly, where each element is attached to its previous and next adjacent elements, is called a linear data structure. Examples are array, stack, queue, etc.
*   **Non-linear Data Structure**: Data structures where data elements are not placed sequentially or linearly are called non-linear data structures. Examples are trees and graphs.

The non-primitive data structures can also be classified based on whether they are built-in or user-defined.

In this Data Structures (Laity Data Structures) Packages we will present the following non primitive data structure:

*   [Installation](#installation)
*   [Stack](#stack)
*   [Queue](#queue)
*   [Linked List](#linked-list)
*   [Tree](https://)


## Installation
* Packages built using [Python]()
* Version : 0.0.2
* To Install it execute the following command line:

  * `pip install laity-data-structures-py`
* Import Any Existing class in your project and Enjoy !

## Stack

Stack is a linear data structure that follows the principle of LIFO (Last In First Out) to store data.
Some basic operations allow us to perform different actions on a stack.

#### Basic operations on stack

*   push() to insert an element into the stack
*   pop() to remove an element from the stack
*   top() Returns the top element of the stack.
*   isEmpty() returns true if the stack is empty else false.
*   size() returns the size of the stack.

In this Packages We firstly implement for the Stack these following functions:
<table>
  <thead>
    <tr>
      <th>Data Structure</th>
      <th> Methods</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Stack</strong></td>
      <td><code>push()</code>, <code>pop()</code>, <code>peek()</code>, <code>is_empty()</code>,<code>size()</code>,<code>display()</code></td>
    </tr>
  </tbody>
</table>

## Queue

Same as Stack, Queue is also a linear data structure. However Queue store data in a FIFO(FIrst In First Out) manner.

#### Basics operations of Queue


*   Enqueue() Adds (or stores) an element to the end of the queue.
*   Dequeue() Removal of elements from the queue.
*   Peek() or front() Acquires the data element available at the front node of the queue without deleting it.
*   rear() This operation returns the element at the rear end without removing it.
*   isFull() Validates if the queue is full.
*   isNull() Checks if the queue is empty.

In this Packages We firstly implement for the Queue data structure these following functions:
<table>
  <thead>
    <tr>
      <th>Data Structure</th>
      <th> Methods</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Queue</strong></td>
      <td><code>enqueue()</code>, <code>dequeue()</code>, <code>peek()</code>, <code>rear()</code>, <code>is_empty()</code>, <code>display()</code></td>
    </tr>
  </tbody>
</table>

## Linked List

A linked list is a linear data structure that includes a series of connected nodes that are not stored at contiguous memory location.

It is represented by a pointer to the first node of the linked list. The first node is called the **head**. If the linked list is empty, then the value of the head is **NULL**. Each node in a list consists of at least two parts:

* Data
* Pointer (Or Reference) to the next node

#### Basic operations



*   Insert: we can insert at the Beginning, Insert at the End, Insert at a Specific Position
*   Delete: we can delete from the Beginning, from the End, at a Specific Position
*   Display: disply by traversing the linked list from the head to the end, visiting each node in turn.
*   Search: look for a node with a specific value or property.
*   Get Length: count the number of nodes.
*   Access: Access data in a specific node by traversing the list or directly indexing if the list supports it.
*   Update: update the data in a specific node by traversing the list to find it and modifying its data.
*   Concatenate: Concatenate two linked lists by making the last node of the first list point to the head of the second list.
*   Reverse: Reverse the order of nodes in the linked list.
*   Sort: Sort the linked list by rearranging nodes according to a specific criterion, such as value or property.


In this Packages We firstly implement for Linked List these following functions:

<table>
  <thead>
    <tr>
      <th>Data Structure</th>
      <th> Methods</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Singly Linked List</strong></td>
      <td><code>head()</code>,<code>insert()</code>,<code>insertAtBeginning()</code>,<code>insertAfter()</code>, <code>delete()</code>, <code>search()</code>, <code>traverse()</code>,<code>display()</code></td>
    </tr>
  </tbody>
</table>

## Tree

### Binary Tree

Tree is a non linear hierarchical data structure where nodes are connected by edges. The binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.


The topmost node is called root and the  bottommost nodes or the nodes with no children are called the leaf nodes. A node contains:

* Data
* Pointer to left child
* Pointer to the right child

In this Packages We firstly implement for the Binary search Tree these following functions:

<table>
  <thead>
    <tr>
      <th>Data Structure</th>
      <th> Methods</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Binary Search Tree (BST)</strong></td>
      <td><code>head()</code>,<code>insert()</code>, <code>search()</code>, <code>printInorder()</code>, <code>printPreOrder()</code>,<code>printPostOrder()</code></td>
    </tr>
  </tbody>
</table>
