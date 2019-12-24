def palindrome(m):
    if m==m[::-1]:
        return True
    else:
        return False

print (palindrome("ere"))
