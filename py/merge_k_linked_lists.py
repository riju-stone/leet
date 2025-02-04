"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Brute Force
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    nodes = []
    for l in lists:
        while l:
            nodes.append(l.val)
            l = l.next

    nodes.sort()
    res = ListNode()
    curr = res
    for node in nodes:
        res.next = ListNode(node)
        res = res.next

    return curr.next


# Divide & Conquer
def merge2Lists(list1, list2):
    res = ListNode(0)
    curr = res
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = ListNode(list1.val)
            list1 = list1.next
        else:
            curr.next = ListNode(list2.val)
            list2 = list2.next

        curr = curr.next

    if list1:
        curr.next = list1

    if list2:
        curr.next = list2

    return res.next


def mergeKLists2(slef, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if len(lists) == 0:
        return None
    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            first_list = lists[i]
            second_list = lists[i + 1] if i + 1 < len(lists) else None

            merged = merge2Lists(first_list, second_list)
            merged_lists.append(merged)
        lists = merged_lists

    return lists[0]
