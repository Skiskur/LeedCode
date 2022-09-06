# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode):
        arr = []

        arr = self.__inorder(root, arr)

        return arr

    def __inorder(self, node: TreeNode, arr):
        if node:
            if node.left:
                arr = self.__inorder(node.left, arr)

            arr.append(node.val)
            if node.right:
                arr = self.__inorder(node.right, arr)

        return arr




if __name__ == '__main__':
    # Input: root = [1, null, 2, 3]
    # Output: [1, 3, 2]

    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    s = Solution()
    result = s.inorderTraversal(root)

    print(result)