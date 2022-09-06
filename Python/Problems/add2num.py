from typing import Optional
import sys

sys.path.append("E:/LeedCode")

from Core import TreeNode as tr


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		treen = tr.list()

		a = treen.to_str(l1)
		b = treen.to_str(l2)

		if len(a) < len(b):
			c = a
			a = b
			b = c
			pass


		for index in range(len(b)):
			a[index] += b[index]

		add = False
		for index in range(len(a)):
			if add:
				a[index] += 1
				add = False
			if a[index] >= 10:
				a[index] -= 10
				add = True

		if add:
			a.append(1)
			
		

		result = treen.create_list(a)

		return result


if __name__ == '__main__':
	s = Solution()
	treen = tr.list()

	one = [9,9,9,9,9]
	two = [9,9,9]

	# one = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
	# two = [5,6,4]


	l1 = treen.create_list(one)
	l2 = treen.create_list(two)

	r = s.addTwoNumbers(l1,l2)

	print(treen.to_str(r))
	
