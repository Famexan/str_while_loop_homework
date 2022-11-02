def main(s):
    """
    juft
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    count = ""

    while i < len(s):
        if s[i].isdigit():
            if int(s[i]) % 2 == 0 and int(s[i]) != 0:
                count += s[i]
        i += 1
        
    count = len(count)
    
    return count

