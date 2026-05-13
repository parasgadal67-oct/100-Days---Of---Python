def palindrome(s):
    """Return True if s is a palindrome, False otherwise."""
    if len (s)<= 1:
        return True
    if s[0] != s[-1]:
        return False
    else:
        return palindrome(s[1:-1])

print(palindrome("hello"))