from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseLinkedList(head: Optional[ListNode]) -> Optional[ListNode]:
    curr_node = head
    prev_node = None

    while head:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node
