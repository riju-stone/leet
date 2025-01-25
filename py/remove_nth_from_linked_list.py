"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 2:
Input: head = [1], n = 1
Output: []

Example 2:
Input: head = [1,2], n = 1
Output: [1]
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    fast = head
    slow = head

    for _ in range(n):
        fast = fast.next

    if not fast:
        return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return head
