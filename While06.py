def main(s):
    """
    undosh
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    
    i = 0
    count = ""
    pun = '''aeiou'''

    while i < len(s):
        if s[i].lower() in pun:
            count += s[i]
        i += 1
        
    count = len(count)
    
    return count
