from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        node = ListNode()
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        a = list1.val
        b = list2.val
        if a <= b:
            node = ListNode(a)
            next1 = list1.next if list1.next else None
            node.next = self.mergeTwoLists(next1, list2)
        else:
            node = ListNode(b)
            next2 = list2.next if list2.next else None
            node.next = self.mergeTwoLists(list1, next2)

        return node
