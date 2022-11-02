def main(s):
    """
    katt hariflar bor
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
 
    i = 0
    count = ""

    while i < len(s):
        if s[i].isupper():
            count += s[i]
        i += 1
        
    count = len(count)
    
    return count
