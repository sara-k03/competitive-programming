def is_palindrome(s):
    return s == s[::-1]

def contains_palindrome(text):
    filtered = ""
    for i in text:
        if ( i.isalpha() ):
            filtered += i.lower()

    n = len(filtered)

    for i in range(n):
        for j in range(i + 2, n + 1):
            if is_palindrome(filtered[i:j]):
                return True
    return False

text = input()

if contains_palindrome(text):
    print("Palindrome")
else:
    print("Anti-palindrome")