"""
Merge two Sorted Linked Lists
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    sorted_list = ListNode()
    curr_node = sorted_list

    while list1 and list2:
        if list1.val < list2.val:
            curr_node.next = list1
            list1 = list1.next
        else:
            curr_node.next = list2
            list2 = list2.next

        curr_node = curr_node.next

    if list1:
        curr_node.next = list1
    else:
        curr_node.next = list2

    return sorted_list
