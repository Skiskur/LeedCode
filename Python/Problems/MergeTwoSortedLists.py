# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_all(self, result, ln):
        if not ln:
            return
        result.append(ln.val)
        if ln.next == None:
            return
        else:
            self.add_all(result, ln.next)

    def create_list(self, result):
        if len(result) != 0:
            ln = ListNode(result[0])
            result.remove(result[0])
            next = self.create_list(result)
            ln.next = next
            return ln
        else:
            return None

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = []
        self.add_all(result, l1)
        self.add_all(result, l2)
        result.sort()
        # result.reverse()
        ln = self.create_list(result)
        return ln


def print_all(ln):
    if ln:
        print(ln.val)
        print_all(ln.next)


if __name__ == '__main__':
    s = Solution()
    # l1 = [1, 2, 4]
    # l2 = [1, 3, 4]
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    result = s.mergeTwoLists(l1, l2)
    print_all(result)
