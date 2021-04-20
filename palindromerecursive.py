def palindrome(a,b=None):
    ''' Recursive palindrome of a word/sentence '''
    if not b:
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        lst = []
        for c in a:
            if c in chars:
                lst.append(c.lower())
        string = "".join(lst)
        length = len(string)
        if length < 2:
            return True
        elif length % 2 == 0:
            return palindrome(string[0:length//2], string[length//2:length])
        else:
            return palindrome(string[0:length//2], string[length//2+1:length])
    else:
        if a[0] == b[len(b)-1]:
            if len(a) > 1:
                return palindrome(a[1:len(a)], b[0:len(b)-1])
            else:
                return True
        else:
            return False

print("Madam", palindrome("Madam"))
print("Nurses run", palindrome("Nurses run"))
print("hello", palindrome("hello"))
print("a", palindrome("a"))
print("abcd", palindrome("abcd"))
print("lol! :)", palindrome("lol! :)"))
print("ldhgsagua;ogbjregu&*(#%'[]  ", palindrome("ldhgsagua;ogbjregu&*(#%'[]  "))
