import sys
from typing import Optional, List

sys.path.append("E:/LeedCode")

from Core import TreeNode as tr


class Solution:
    def mergeKLists(self, lists: List[Optional[tr.ListNode]]) -> Optional[tr.ListNode]:
        ls = tr.list()
        result = []

        for node in lists:
            result += ls.to_str(node)

        result.sort()
            
        return ls.create_list(result)



if __name__ == '__main__':
    s = Solution()

    ls = tr.list()

    data = []

    l1 = ls.create_list([1,4,5])
    l2 = ls.create_list([1,3,4])
    l3 = ls.create_list([2,6])

    data.append(l1)
    data.append(l2)
    data.append(l3)

    print(ls.to_str(s.mergeKLists(data)))
