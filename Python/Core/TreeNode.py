# import sys

# sys.path.append("E:/LeedCode")

# from Core import TreeNode as tr

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class tree:
	def to_tree(self, arr: []):
		if not arr:
			return None
		if arr[0] == None:
			arr.pop(0)
			return None
		return TreeNode(
			val=arr.pop(0),
			left=self.to_tree(arr),
			right=self.to_tree(arr)
		)

	def to_str(self, root):
		arr= []
		arr = self.__str(root, arr)

		while arr[len(arr)-1] == None:
			arr.pop(len(arr)-1)

		return arr

	def __str(self, root, arr):
		if root:
			arr.append(root.val)
			arr = self.__str(root.left, arr)
			arr = self.__str(root.right, arr)
		else:
			arr.append(None)
		return arr



class list:

	def create_list(self, result: []):
		if len(result) != 0:
			ln = ListNode(result[0])
			result.remove(result[0])
			next = self.create_list(result)
			ln.next = next
			return ln
		else:
			return None

	def to_str(self, root):
		arr= []
		arr = self.__str(root, arr)

		return arr

	def __str(self, root, arr):
		if root:
			arr.append(root.val)
			arr = self.__str(root.next, arr)            
		
		return arr