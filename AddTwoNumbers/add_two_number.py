
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        def dfs(n1, n2, carry):
            if n1 is None and n2 is None and carry == 0:
                return None

            a = n1.val if n1 else 0
            b = n2.val if n2 else 0

            total = a + b + carry
            digit = total % 10
            new_carry = total // 10

            node = ListNode(digit)

            next1 = n1.next if n1 else None
            next2 = n2.next if n2 else None

            node.next = dfs(next1, next2, new_carry)
            return node

        return dfs(l1, l2, 0)