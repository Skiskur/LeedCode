import sys
from typing import Optional

sys.path.append("E:/LeedCode")

from Core import TreeNode as tr


class Solution:
    def reverseKGroup(self, head: Optional[tr.ListNode], k: int) -> Optional[tr.ListNode]:

        ls = tr.list()

        arr = ls.to_str(head)

        result = []
        hlam = []

        for i in range(0,len(arr),k):
            lenght = i + k if i+k<len(arr) else len(arr)
            for m in range(i, lenght):
                hlam.append(arr[m])

            if len(hlam) == k:
                hlam.reverse()
            result += hlam
            hlam = []

        return ls.create_list(result)


if __name__ == '__main__':
    s = Solution()

    ls = tr.list()


    l1 = ls.create_list([1])
    k = 1
    

    print(ls.to_str(s.reverseKGroup(l1, k)))