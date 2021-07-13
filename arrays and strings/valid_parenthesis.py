"""
Initial idea: use a stack.
Add to the stack open parenthesis always. When you encounter a closed
parenthesis, check to see if the end of the queue is the same type of
parenthesis. If it is, pop that element from the queue.
If it's not, return false. If the queue in the end is empty return

time -> O(N)
space -> O(N)
"""


def is_valid(s: str) -> bool:
    # If it's an odd length then it cannot be valid
    if len(s) % 2 == 1:
        return False

    stack = []
    open_types = ["(", "{", "["]
    closed_types = [")", "}", "]"]

    for parenthesis in s:
        if parenthesis in open_types:
            stack.append(parenthesis)
        # Closed and empty means there is guys at the end
        elif len(stack) == 0:
            return False
        # Closed and stack not empty
        else:
            # There might be a better way to write this but whatever haha
            last_elem = stack.pop()
            open_index = open_types.index(last_elem)
            expected_closed = closed_types[open_index]
            if expected_closed != parenthesis:
                return False

    # If the stack is not empty at the end means there is parenthesis at the end
    return len(stack) == 0
