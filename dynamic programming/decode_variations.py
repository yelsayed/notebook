# This is a note to study the decode variations dynamic programming question
# https://leetcode.com/problems/decode-ways/

# The question asks if you can find the variations of an encoded string given
# that the encoding could be multiple things.
# The encoding is '1' -> 'A', '2' -> 'B' ... '26' -> 'Z'.
# For a string '1262' it could be 'AZB', 'ABFB', and 'LFB'.

# Our job is to find how many ways this string CAN be decoded, without actually
# decoding it.

# Some things to note before we start.
# 1) The max number is 26, so any encoding bigger than that doesn't count.
# 2) Some encodings are incorrect for example '1270' has no encodings because 0
#    doesn't map to anything
# 3) An ambiguous encoding starts with either a '1' or a '2', which simplifies
#    the problem a little

# Let's get started with the coding
# Initial Solution
# Idea: This seems like a hard problem to optimize, the efficient solution isn't
#       very obvious off the bat. But since there isn't much iteration that we
#       need to go through, perhaps the initial solution isn't so bad. My
#       initial idea is to go through the string and build a list of lists that
#       can be used to count the number of variations. For the example '1262' I
#       can break it up into [[1], [1,2], [2], [2,6], [2]].

# In a vertical repr this looks like
# [
#  [1], [1,2],
#  [2], [2,6],
#  [6],
#  [2]
# ]

# This allows us to pop things from it and iterate over it while counting how
# many are at the base case. The major downside of this is that it's too tough
# to code.

def breakUp(S):
    ret = []
    # Here we iterate breaking it up based on the value
    for index, char in enumerate(S):
        # There will always be one way to decode the last element
        if index == len(S) - 1:
            ret.append((char))
        # If the char is '1' then we know there are two paths we should take
        elif char == '1':
            ret.append((char, char + S[index + 1]))

        # If the char is '2' then there is only two ways if the next char is < 7
        elif char == '2':
            if int(S[index + 1]) <= 6:
                ret.append((char, char + S[index + 1]))
            else:
                ret.append((char,))
    return ret


def _decode_variations_bad(S, count):
    if len(S) == 1:
        return count + 1

    # two paths here
    if len(S[0]) == 2:
        S[0] = (S[0][0])
        return _decode_variations_bad(S, count) + 1

    # only one path here
    if len(S[0]) == 1:
        return _decode_variations_bad(S[1:], count)


def decode_variations_bad(S):
    broken_s = breakUp(S)
    return _decode_variations_bad(broken_s, 0)


# The reason this solution doesn't work is just because of the emphasis
# on breaking up the string into a list of lists. We don't need to get all the
# variations, if we did, then my solution would be more palatable. Currently,
# also counting out the bad strings is more difficult given this data structure.

# One realization that helped me with this solution is just that the number
# of paths for one string depends on the number of paths for the next string.

def decode_variations(string):
    if len(string) == 1:
        if string[0] == '0':
            return 0
        return 1

    if len(string) == 2:
        if string[0] == '1':
            return 2
        if string[0] == '2' and int(string[1]) <= 6:
            return 2
        if string[0] == '2' and int(string[1]) > 6:
            return 1

    if string[0] == '1':
        return decode_variations(string[1:]) + \
               decode_variations(string[2:])

    if string[0] == '2':
        return decode_variations(string[1:]) + \
               (decode_variations(string[2:]) if int(string[2]) <= 6 else 0)

    # Last case where it's 0
    return decode_variations(string[1:])


# Lastly, we can do this using Dynamic programming.
# The realization I made earlier that the number of paths for one string is
# dependant on the number of paths for the last string, this indicates that
# you can solve this problem using Dynamic programming.

# Our objective is just to count the number of ways, so we can create a
# dynamic programming array that "passes the baton" so to speak.
# The logic is as follows:
# 0 - If the first integer is 0, there are no variations to be decoded
# 1 - If the current digit is not 0, this means there is one way to decode it.
# 2 - If the two digits are between 10 and 26 then we know there is more ways to
# decode than one. This means that it's the number of ways of decoding this one
# digit (which we know isn't 0) plus the number of ways of decoding the last
# step.

def decode_variations_dp(s: str) -> int:
    # If the first integer is 0, it's kind of moot to try and find a variation
    if s[0] == '0':
        return 0

    dp = [0] * (len(s) + 1)
    # The batons, has to be 2 since we're starting with 2 in the loop
    dp[0] = 1
    dp[1] = 1

    for i in range(2, len(dp)):
        # The two digit integer
        full_int = int(s[i - 2: i])
        # The digit we're currently on
        first_int = int(s[i - 1])

        # If the current digit is 0, we shouldn't pass the baton, and perhaps
        # it will be counted in the two digit phase
        if first_int != 0:
            dp[i] = dp[i - 1]

        # If the two digit is within bounds then we should add the current digit
        # ways (done in the last step) to the two digit ways done one step back
        if 10 <= full_int <= 26:
            dp[i] += dp[i - 2]
    return dp[-1]
