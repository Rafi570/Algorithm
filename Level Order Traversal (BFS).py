from collections import deque
from typing import Optional

class Node:
    def __init__(self, info: int): 
        self.info = info  
        self.left: Optional[Node] = None  
        self.right: Optional[Node] = None 
        self.level: Optional[int] = None 

    def __str__(self) -> str:
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root: Optional[Node] = None

    def create(self, val: int) -> None:  
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def levelOrder(root: Optional[Node]) -> None:
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.info, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example usage:
tree = BinarySearchTree()
t = int(input("Enter the number of nodes: "))
arr = list(map(int, input("Enter the node values: ").split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)
