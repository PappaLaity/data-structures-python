# 🔗 Linked List – Data Structure

A **Linked List** is a linear data structure composed of a sequence of connected nodes.  
Unlike arrays, the elements (nodes) in a linked list are **not stored in contiguous memory locations**.

A linked list is represented by a pointer to its first node, known as the **head**.  
If the list is empty, the head points to **NULL**.

Each node typically contains two components:
- 📦 **Data** – The value held by the node  
- 🧭 **Pointer** – A reference to the next node in the sequence  

---

## ⚙️ Basic Linked List Operations

Here are the most common operations performed on a linked list:

- ➕ **Insert**: Add a node at the beginning, at the end, or at a specific position  
- ➖ **Delete**: Remove a node from the beginning, the end, or a specific position  
- 👁️ **Display**: Traverse the list from the head to the end, visiting each node in order  
- 🔍 **Search**: Look for a node containing a specific value or property  
- 📏 **Get Length**: Count the number of nodes in the list  
- 📂 **Access**: Retrieve data from a specific node by traversing the list  
- 📝 **Update**: Modify the data of a specific node by locating and updating it  
- 🔗 **Concatenate**: Join two linked lists by linking the last node of the first to the head of the second  
- 🔁 **Reverse**: Reverse the order of the nodes in the list  
- 🔢 **Sort**: Rearrange the nodes based on a given value or property  

---

## 🧪 Implemented Methods

This package includes an implementation of the following methods for a **Singly Linked List**:

| 🗃️ Data Structure        | 🛠️ Available Methods                                                                                   |
|--------------------------|--------------------------------------------------------------------------------------------------------|
| **Singly Linked List**   | `head()`, `insert()`, `insertAtBeginning()`, `insertAfter()`, `delete()`, `search()`, `traverse()`, `display()` |

> 📌 **Note**: These functions allow full control over list management, from basic insertion to advanced operations like reversal and concatenation.

---
