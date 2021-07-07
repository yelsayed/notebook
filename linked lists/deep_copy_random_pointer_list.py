"""
Note on Deep Copy Linked List with Random Pointers
https://leetcode.com/problems/copy-list-with-random-pointer/

I'm coming back to this question after solving it 27 days ago so I don't
remember my initial solution, but I remember struggling with it.

The final idea:
Weave the lists together. Weaving the lists together just means that you copy
each node of the linked list over without copying the pointers. Then you can
go through the linked list one more time and carry over the random pointers
of your node to the next node.

Note:
The problem with a question like this is that you could get stuck chasing
your tail with random pointers. When you have a question like this that's
very messy, it's easiest to just think simply or come up with more and more
overarching methods.

Example:
[1] -> [2] -> [3]
Where 1 points to 3 and 2 points to 1 randomly.

You can add to this linked list
[1] -> [1] -> [2] -> [2] -> [3] -> [3]

While not copying over the random pointers. Then go through it again, this time
we know that the even nodes are the duplicates and the odd ones aren't,
so at every odd point add the random pointer of your next to be your own.

And this works like a charm

Complexity
Time -> O(N)
Space -> O(1) because you're not really adding to the memory usage in your
              solution (this is bullshit btw but that's what they want us to say)
"""


class Node:
    """ Strict definition, you cannot change this """

    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(val)
        self.next = next
        self.random = random


def duplicate_next(node: Node):
    if node is None:
        return

    duplicate_next(node.next)

    new_node = Node(val=node.val)

    new_node.next = node.next
    node.next = new_node


def copy_random_list(head: Node) -> Node:
    # Duplicate the linked list without random
    duplicate_next(head)
    current = head
    index = 0

    while current:
        next_node = current.next

        # If your counter is even this means you're at an original node so you
        # should move the random pointer of the node ahead of you to your
        # random pointer's next (since you're creating a new list)
        if index % 2 == 0 and current.random is not None:
            current.next.random = current.random.next
        if index % 2 == 1 and current.next is not None:
            current.next = current.next.next

        current = next_node
        index += 1

    return head.next if head else None
