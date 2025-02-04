"""
Given the head of a singly linked list and two integers left and right where left <= right,
reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(
    head: Optional[ListNode], left: int, right: int
) -> Optional[ListNode]:
    if not head or left > right:
        return head

    dummy = ListNode(0, head)
    prev_node = dummy

    # point to left - 1 node
    for _ in range(left - 1):
        prev_node = prev_node.next

    # node at left
    curr = prev_node.next
    for _ in range(right - left):
        next_node = curr.next
        curr.next = next_node.next
        next_node.next = prev_node.next
        prev_node.next = next_node

    return dummy.next
