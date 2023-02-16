# converting string into integer:
# base case: if len of string is 0 return 0
#             if len of string is 1 return int(string)
# assume for all l - 1 length it's true : convert(string[1:])
# induction step: add a[0] times 10 raised to the power of l - 1 to the convert(a[1:])


def convert(string):
    l = len(string)
    if not string:
        return 0
    if l == 1:
        return int(string)
    ans = convert(string[1:])

    return int(string[0])*(10**(l - 1)) + ans


def trim(string):
    return string.lstrip('0')

string = input()
string = trim(string)
integer = convert(string)
print(integer)


# The program takes an input string, which is a string of digits representing a number.
# The trim function is used to remove any leading zeros in the input string.

# The convert function is a recursive function that takes a string as input
# and converts it to the corresponding integer.
# If the input string is empty, the function returns 0. 
# If the input string has only one character, the function returns the integer value of that character. 
# Otherwise, the function makes a recursive call to convert
# with the substring of the input string starting from the second character, 
# and adds the value of the first character multiplied by 10 raised to the power of the length
# of the input string minus one to the result of the recursive call.

# After the input string is trimmed to remove any leading zeros, 
# the convert function is called with the trimmed string as input, 
# and the resulting integer is printed as output.
