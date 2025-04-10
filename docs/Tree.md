# Tree Data Structure

## Binary Tree

A **Tree** is a non-linear hierarchical data structure composed of nodes connected by edges. 

A **Binary Tree** is a specific type of tree where each node has at most two children, referred to as:
- **Left Child**
- **Right Child**

### Key Components

- **Root**: The topmost node in the tree
- **Leaf Nodes**: The bottommost nodes (nodes without any children)
- **Node Structure**:
  - Data
  - Pointer to left child
  - Pointer to right child

## Binary Search Tree (BST) Implementation

In this package, we implement the following functions for a Binary Search Tree:

| Data Structure          | Methods                                                                                     |
|-------------------------|---------------------------------------------------------------------------------------------|
| **Binary Search Tree**  | `head()`, `insert()`, `search()`, `printInorder()`, `printPreOrder()`, `printPostOrder()`  |

### Tree Traversal Methods

1. **Inorder Traversal**: Left → Root → Right
2. **Preorder Traversal**: Root → Left → Right
3. **Postorder Traversal**: Left → Right → Root
