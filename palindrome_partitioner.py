def is_palindrome(string: str) -> bool:
    return string == string[::-1]

def palindrome_cut(string: str) -> int:
    cut = 0
    i = 0
    while i < len(string):
        for j in range(len(string), i, -1):  
            if is_palindrome(string[i:j]):
                if j != len(string):
                    cut += 1
                i = j
                break
    return cut


print(palindrome_cut("abbaanna"))