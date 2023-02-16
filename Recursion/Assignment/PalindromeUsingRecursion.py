#Palindrome using Recursion:
#1: base case -> if length of string is one or zero return the true
#2: check if a[0] == a[len - 1] if yes then call the function on string[1:-1]
    else return false.


string  = 'racecar'

def pdrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
    if string[0] == string[-1]:
        return pdrome(string[1:-1])
    else:
        return False


print(pdrome(string))