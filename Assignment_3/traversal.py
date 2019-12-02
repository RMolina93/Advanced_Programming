# A recursive Python program to print REVERSE level order traversal 

#Let's define a Node for creating the tree.
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

# Print the nodes of a binary tree in a reverse level order
def ReverseLevelOrderTraversal(root): 
    Stack = [] 
    Queue = [] 
    Queue.append(root) 
  
    while (len(Queue) > 0): 
        root = Queue.pop(0) 
        Stack.append(root) 
  
        if (root.right): 
            Queue.append(root.right) 
  
        if (root.left): 
            Queue.append(root.left) 
  
    # Now print all items from the stack
    while (len(Stack) > 0): 
        root = Stack.pop() 
        print root.data,

#Let's test it.
root = Node("A") 
root.left = Node("B") 
root.right = Node("C") 
root.left.left = Node("D") 
root.left.right = Node("E") 
root.right.left = Node("F") 
root.right.right = Node("G") 
  
print "The Reverse Level Order Traversal for this tree is: "
ReverseLevelOrderTraversal(root) 

