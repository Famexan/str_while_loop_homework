import string
def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer

    """

    i = 0
    count = ""
    pun = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    while i < len(s):
        if i in pun:
            count += s[i]
        i += 1
        
    count = len(count)
    
    return count