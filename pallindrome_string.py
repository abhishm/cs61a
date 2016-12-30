def pallindrome(s):
    """Return the largest pallindrome in the string
    >>> pallindrome("abcba")
    'abcba'
    >>> pallindrome("abcbd")
    'bcb'
    """
    if len(s) <= 1:
        return s
    elif s[0] != s[-1]:
        begining_pallindrome = pallindrome(s[:-1])
        ending_pallindrome = pallindrome(s[1:])
        if len(begining_pallindrome) >= len(ending_pallindrome):
            return begining_pallindrome
        else:
            return ending_pallindrome
    else:
        middle_pallindrome = pallindrome(s[1:-1])
        if len(middle_pallindrome) == len(s[1:-1]):
            return s[0] + middle_pallindrome + s[-1]
        else:
            return middle_pallindrome

def pallindrome2(s):
    """Return the largest in a string in O(n**2) time and constant memory
    >>> pallindrome2("abcba")
    'abcba'
    >>> pallindrome2("abcbd")
    'bcb'
    >>> pallindrome2("hackerrekcahba")
    'hackerrekcah'
    """
    def pallindrome_at_i(s, i):
        """Return the starting position and length of the largest pallindrome string
        starting from position i
        >>> pallindrome_at_i("abcbd", 0)
        (0, 1)
        >>> pallindrome_at_i("abcbd", 2)
        (1, 3)
        >>> pallindrome_at_i("abcbd", 1)
        (1, 1)
        >>> pallindrome_at_i("abbd", 1)
        (1, 2)
        >>> pallindrome_at_i("abcbb", 2)
        (1, 3)
        """
        lower_lim = i
        upper_lim = i
        is_pallindrome = True
        if lower_lim >= 1 and upper_lim < len(s) - 1 and s[lower_lim - 1] == s[upper_lim + 1]:
            lower_lim -= 1
            upper_lim += 1
        elif upper_lim < len(s) - 1 and s[lower_lim] == s[upper_lim + 1]:
            upper_lim += 1
        else:
            return lower_lim, (upper_lim - lower_lim + 1)
        while lower_lim >= 1 and upper_lim < len(s) - 1:
            if s[lower_lim - 1] == s[upper_lim + 1]:
                lower_lim -= 1
                upper_lim += 1
            else:
                return lower_lim, (upper_lim - lower_lim + 1)
        return lower_lim, (upper_lim - lower_lim + 1)

    start_max_pallindrome = 0
    len_max_pallindrome = 0
    for i in range(len(s)):
        start, length = pallindrome_at_i(s, i)
        if length > len_max_pallindrome:
            start_max_pallindrome, len_max_pallindrome = start, length

    return s[start_max_pallindrome:start_max_pallindrome + len_max_pallindrome]
