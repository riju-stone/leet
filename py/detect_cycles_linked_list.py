"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached
again by continuously following the next pointer.
Return true if there is a cycle in the linked list. Otherwise, return false.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: Optional[ListNode]) -> bool:
    # hash method
    # curr_node = head
    # visited_nodes = set()

    # while curr_node:
    #     if curr_node in visited_nodes:
    #         return True
    #     visited_nodes.add(curr_node)
    #     curr_node = curr_node.next
    # return False

    # two pointers (floyd's cycle detection or turtle-hare algorithm)
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
