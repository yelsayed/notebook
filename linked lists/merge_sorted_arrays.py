"""
Note on Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

The problem is to merge two linked lists that are sorted to get a combined
sorted linked list.

The problem is very simple, just keep two pointers and merge them like we
do with merge sort.

Complexity:
Time -> O(N)
Space -> O(N) You're building a new one
"""

from typing import Union


class ListNode:
    def __init__(self, val: Union[int, None] = 0, next=None):
        self.val = val
        self.next = next


def _merge_two_lists(l1: ListNode, l2: ListNode,
                     final_node: ListNode) -> Union[ListNode, None]:
    next_node = ListNode(val=None)
    val1 = getattr(l1, 'val', 101)
    val2 = getattr(l2, 'val', 101)

    if val1 <= val2:
        final_node.val = val1
        l1 = getattr(l1, 'next', None)
    else:
        final_node.val = val2
        l2 = getattr(l2, 'next', None)

    if l1 is None and l2 is None:
        return

    final_node.next = next_node

    _merge_two_lists(l1, l2, final_node.next)


def merge_two_lists(l1: ListNode, l2: ListNode) -> Union[ListNode, None]:
    final_node = ListNode()

    if l1 is None and l2 is None:
        return None

    _merge_two_lists(l1, l2, final_node)

    return final_node
