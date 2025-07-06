class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
newTreeNode= TreeNode(10,2,5)
newTreeNode1= TreeNode(None,10, 2)

def check_tree(root):
    if root.left * root.right == root.val:
        return True
    else:
        return False

# print(check_tree(newTreeNode))
# print(check_tree(newTreeNode1))

def check_tree_new(root):
    if root.left and root.right and root.val:
        if root.left * root.right == root.val:
            return True
        else:
            return False
    else:
        return False
# print(check_tree_new(newTreeNode))

#Input Tree
rightMostTree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))
rightMostTreeDegen = TreeNode(1, TreeNode(2, TreeNode(4), None), TreeNode(5))
bstleafTree = TreeNode(4, TreeNode(2, TreeNode(1), 3), TreeNode(5))
rightMostTree1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))

def right_most_iterative(root):
    while root.right:
        root = root.right
    return root.val

# print(right_most_iterative(rightMostTree))
# print(right_most_iterative(rightMostTree1))

def right_most_recursive(root):
    if root.right == None:
        return root

    return right_most_recursive(root.right)

# print(right_most_recursive(rightMostTree).val)
# print(right_most_recursive(rightMostTree1).val)

def postorder_traversal(root): #left Right Middle
    result = []
    def postorder_DFS(node):
        if node == None:
            return 
        postorder_DFS(node.left)
        postorder_DFS(node.right)
        result.append(node.val)
    postorder_DFS(root)
    return result
    
# print(postorder_traversal(rightMostTree))

def preorder_traversal(root): #Middle Left Right
    result = []
    
    def preorder_traversalDFS(node):
        if node == None:
            return
        result.append(node.val)
        preorder_traversalDFS(node.left)
        preorder_traversalDFS(node.right)
    preorder_traversalDFS(root)
    return result
# print(preorder_traversal(rightMostTree))

def inorder_traversal(root): #Left Middle Right
    result = []
    
    def inorder_traversalDFS(node):
        if node == None:
            return
        
        inorder_traversalDFS(node.left)
        result.append(node.val)
        inorder_traversalDFS(node.right)
    
    inorder_traversalDFS(root)
    return result

# print(inorder_traversal(rightMostTree))

#Where left is called before right for these tree traversals
#PRE - .val called first
#IN - .val called second
#Post - .val called third

def product_tree(root):
    result = []
    productTotal = 1
    
    def tree_traversal(node):
        if node == None:
            return
        result.append(node.val)
        tree_traversal(node.left)
        tree_traversal(node.right)
    
    tree_traversal(root)
        
    for number in result:
        productTotal = productTotal * number
        
    return productTotal

# print(product_tree(rightMostTree))


def is_leaf(root):
    
    myList = [True]
    
    def tree_traversal(root):
        if root == None:
            return
        if root.left == None and root.right == None:
            return
        
        if (root.left and root.right == None) or (root.right and root.left == None):
            myList.append(False)
        tree_traversal(root.left)
        tree_traversal(root.right)
    
    tree_traversal(root)

    if len(myList) >= 2:
        return False
    else:
        return True
    
# print(is_leaf(rightMostTree))
# print(is_leaf(rightMostTreeDegen))

def is_leaf_bst(root, value): 
    def find_node(node):
        if node is None:
            return False
        if node.val == value:
            return node.left is None and node.right is None
        elif value < node.val:
            return find_node(node.left)
        else:
            return find_node(node.right)

    return find_node(root)


print(is_leaf_bst(bstleafTree,6))