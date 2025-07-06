class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    if not root:
        return True
    
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (
            t1.val == t2.val and
            is_mirror(t1.left, t2.right) and
            is_mirror(t1.right, t2.left)
        )
    
    return is_mirror(root.left, root.right)

symmetricTree = TreeNode(1, TreeNode(2,TreeNode(3),TreeNode(4)), TreeNode(2,TreeNode(4),TreeNode(3)))

# print(is_symmetric(symmetricTree))


#Must create a string and append to a list where the root node goes to all leaf nodes
# To find a leaf node we check can add nodes to a stack indicating the path that we have taken to find the leaf
# We can then append this as a string to the list

def binary_tree_paths(root):
    myList = []
    myStack = []
    def find_path(node): #Return a list
        if node is None:
            return
        
        myStack.append(find_path(node.left))
        myStack.append(find_path(node.right))
        
        for item in myStack:
            myList.append(item.val)
        myList.append("EOF")
        myStack.clear()
    
    find_path(root)
    
    return myList

# print(binary_tree_paths(symmetricTree))

#Traverse tree starting with the left side if it exists and hold two minimum values in the main function for sol
def min_diff_in_bst(root):
    if root is None:
        return
    
    myList = []
    def bstMinTraversal(node):
        if node is None:
            return
        myList.append(node.val)
        bstMinTraversal(node.left)
        bstMinTraversal(node.right)
    
    bstMinTraversal(root)
    
    myList.sort()
    minDiff = myList[0] # Will be here bc root was already checked for null
    if len(myList) >= 2:
        minDiff = myList[1] - myList[0]
        
    return minDiff

# print(min_diff_in_bst(symmetricTree))

#Level order traversal
levelOrderTree = TreeNode(4, TreeNode(2,TreeNode(1),TreeNode(3)), TreeNode(6))
levelOrderTree1 = TreeNode()
levelOrderTree1.left = TreeNode(2)
levelOrderTree1.right = TreeNode(3)
from collections import deque
def level_order(root):
    # If the tree is empty:
    # return an empty list
    if root is None:
        return []

    # Create an empty queue using deque
    # Create an empty list to store the explored nodes
    queue = deque()
    exploredList = []

    # Add the root to the queue
    queue.append(root)

    # While the queue is not empty:
    # Pop the next node off the queue (pop from the left side!)
    # Add the popped node to the list of explored nodes
    while queue:
        removed_ele = queue.popleft()
        exploredList.append(removed_ele)

        # Add each of the popped node's children to the end of the queue
        if removed_ele.left:
            queue.append(removed_ele.left)
        if removed_ele.right:
            queue.append(removed_ele.right)

    # Return the list of visited nodes
    return exploredList

myFunc = level_order(levelOrderTree1)
for item in myFunc:
    print(item.val, end=' ')
    
levelOrderTree = TreeNode(1,None,TreeNode(2,None,TreeNode(3,None,TreeNode(4,None,TreeNode(5, None,TreeNode(6))))))

def min_depth(root):
    # If the tree is empty:
    # return an empty list
    if root is None:
        return []

    # Create an empty queue using deque
    # Create an empty list to store the explored nodes
    queue = deque()
    exploredList = []

    # Add the root to the queue
    queue.append(root)

    depthVar = 0
    # While the queue is not empty:
    # Pop the next node off the queue (pop from the left side!)
    # Add the popped node to the list of explored nodes
    while queue:
        removed_ele = queue.popleft()
        exploredList.append(removed_ele)
        #Found minimum depth
        if removed_ele.left is None and removed_ele.right is None:
            break
        # Add each of the popped node's children to the end of the queue
        if removed_ele.left:
            queue.append(removed_ele.left)
        if removed_ele.right:
            queue.append(removed_ele.right)
        depthVar += 1

    return depthVar

# print(min_depth(levelOrderTree1))