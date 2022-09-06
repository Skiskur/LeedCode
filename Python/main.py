from Core import TreeNode as t
from Problems import MaximumDepthofBinaryTree as problem


if __name__ == '__main__':
    func = t.func()
    s = problem.Solution()

    arr = [3,9,20,None,None,15,7]

    result = func.to_tree(arr)

    result = t.TreeNode(3, t.TreeNode(9), t.TreeNode(20, t.TreeNode(15), t.TreeNode(7)))

    print(func.to_str(result))
    print(s.maxDepth(result))