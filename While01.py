def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = len(s)
    count = 0
    while i > 0:
        i -= 1
        if s[i].isdigit():
            count += 1

    if count == len(s):
        s = int(s)
        return s



