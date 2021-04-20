def palindrome(string):
    ''' Find palindrome of a word/setence (without punctuation) '''
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    lst = []
    for c in string:
        if c in chars:
            lst.append(c.lower())
    length = len(lst)
    for i in range(length//2):
        if lst[i] != lst[length-1-i]:
                return False
    return True

print(palindrome("hello"))
print(palindrome("lol"))
print(palindrome("a"))
print(palindrome("abcd"))
print(palindrome("...!!4929ellle"))
print(palindrome("madam!"))
