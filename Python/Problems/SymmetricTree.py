# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def to_tree(arr: []):
    if not arr:
        return None
    if arr[0] == None:
        arr.pop(0)
        return None
    return TreeNode(
        val=arr.pop(0),
        left=to_tree(arr),
        right=to_tree(arr)
    )




class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        root.right = self.mirror(root.right)

        if self.to_str(root.left) != self.to_str(root.right):
            return False

        return True


    def to_str(self, root):
        arr= []
        arr = self.__str(root, arr)
        return arr

    def __str(self, root, arr):
        if root:
            arr.append(root.val)
            arr = self.__str(root.left, arr)
            arr = self.__str(root.right, arr)
        else:
            arr.append(None)
        return arr

    def mirror(self, root: TreeNode):
        if root:
            if root.left:
                self.mirror(root.left)
            if root.right:
                self.mirror(root.right)
            val = root.left
            root.left = root.right
            root.right = val
        return root

# IndentationError: expected an indented block
#     ^
#     root.right = self.mirror(root.right)
# Line 10  (Solution.py)



if __name__ == '__main__':
    s = Solution()

    arr = [1,2,2,3,4,4,3]

    tree = to_tree(arr)
    tree = TreeNode(1, TreeNode(2, TreeNode(3),TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))

    result = s.isSymmetric(tree)

    print(result)
