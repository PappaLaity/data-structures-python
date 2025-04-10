# 🌿 Laity Data Structures

[![Version](https://img.shields.io/badge/version-0.1.2-blue.svg)](https://pypi.org/project/laity-data-structures/)
[![Python](https://img.shields.io/badge/python-3.7%2B-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-brightgreen)](./LICENSE)

**Laity Data Structures** is a Python package that provides simple and educational implementations of essential non-primitive data structures such as stacks, queues, linked lists, and binary search trees.

Whether you're a student, a developer preparing for interviews, or someone curious about how data structures work under the hood — this package is for you.

---

## ✨ Features

- ✅ Easy-to-read Python code
- 🧱 Stack, Queue, Linked List, Binary Search Tree implementations
- 📘 Educational method names and documentation
- 📦 Simple pip installation
- 🎓 Ideal for learning & teaching

---

## 📦 Installation

```bash
pip install laity-data-structures
```

Once installed, you can import any class into your project:

```python
from laity.stack import Stack

s = Stack()
s.push(10)
s.push(20)
s.display()  # Output: [10, 20]
```

---

## 🧰 Data Structures Included

### 🔁 Stack

A **Last-In, First-Out (LIFO)** linear data structure.

```python
stack.push(value)
stack.pop()
stack.peek()
stack.is_empty()
stack.size()
stack.display()
```

---

### 📤 Queue

A **First-In, First-Out (FIFO)** linear structure for sequential data processing.

```python
queue.enqueue(value)
queue.dequeue()
queue.peek()
queue.rear()
queue.is_empty()
queue.display()
```

---

### 🔗 Singly Linked List

A series of nodes connected using pointers. Efficient for insertions and deletions.

```python
linked_list.insert(value)
linked_list.insertAtBeginning(value)
linked_list.insertAfter(index, new_value)
linked_list.delete(value)
linked_list.search(value)
linked_list.traverse()
linked_list.display()
```

---

### 🌳 Binary Search Tree (BST)

A hierarchical structure where each node has at most two children. Left child < node < right child.

```python
bst.insert(value)
bst.search(value)
bst.printInOrder()
bst.printPreOrder()
bst.printPostOrder()
```

---

## 📂 Project Structure

```
laity-data-structures-py/
│
├── laity/
│   ├── stack.py
│   ├── queue.py
│   ├── linked_list.py
│   ├── tree.py
│
├── examples/
│   ├── stack_test.ipynb
│   ├── queue_test.ipynb
│   ├── linked_list_test.ipynb
│   ├── tree_test.ipynb
│
├── README.md
├── setup.py
└── LICENSE
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

---

## 🙌 Acknowledgements

Created with ❤️ by [PappaLaity](https://github.com/PappaLaity)  
Inspired by educational goals and the love of clean, simple code.

---

## 🚀 Ready to Explore?

Install it, play with it, modify it — and level up your understanding of data structures one line at a time.

```bash
pip install laity-data-structures
```
