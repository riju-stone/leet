from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    slow, fast = head, head

    # slow will be at the mid and fast will be at the end
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the second half
    second_half = None
    curr_node = slow.next

    while curr_node:
        temp = curr_node.next
        curr_node.next = second_half
        second_half = curr_node
        curr_node = temp

    # detach the first half
    slow.next = None

    # merge two halves
    first_half = head

    while second_half:
        first_next, second_next = first_half.next, second_half.next
        first_half.next = second_half
        second_half.next = first_next

        first_half = first_next
        second_half = second_next
