def main(s):
    """
    kichkina
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    count = ""

    while i < len(s):
        if s[i].islower():
            count += s[i]
        i += 1
        
    count = len(count)
    
    return count
