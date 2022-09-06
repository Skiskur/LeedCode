from Core import TreeNode

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        result = self.__depth(root)
        return result

    # arr = [1, 2, 2, 3, 4, 4, 3]
    def __depth(self, root, depth=-1):
        if root:
            depth += 1
            first = self.__depth(root.left, depth)
            second = self.__depth(root.right, depth)
            if first < second:
                first = second
            depth = first
        return depth