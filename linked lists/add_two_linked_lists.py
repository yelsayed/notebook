"""
Note on Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

The idea here is just elementary math. Whenever adding two digits is more than
10, propagate the one down the chain of one of the linked lists.

Then at the end add all the remaining digits from either that are left over.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_to_node(l: ListNode) -> None:
    """ Propogates the carrying of the 1 """
    new_val = l.val + 1
    if new_val <= 9:
        l.val = new_val
        return

    l.val = 0

    if l.next is None:
        l.next = ListNode()

    add_to_node(l.next)


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    res = ListNode()
    ptr = res
    before_last_ptr = None

    while l1 is not None and l2 is not None:
        val = l1.val + l2.val

        if val > 9:
            val = val - 10

            if l1.next is None:
                l1.next = ListNode()

            add_to_node(l1.next)

        ptr.val = val

        ptr.next = ListNode()
        before_last_ptr = ptr
        ptr = ptr.next
        l1 = l1.next
        l2 = l2.next

    while l1 is not None:
        ptr.val = l1.val

        ptr.next = ListNode()
        before_last_ptr = ptr
        ptr = ptr.next
        l1 = l1.next

    while l2 is not None:
        ptr.val = l2.val

        ptr.next = ListNode()
        before_last_ptr = ptr
        ptr = ptr.next

        l2 = l2.next
    before_last_ptr.next = None
    return res
