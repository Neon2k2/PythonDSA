# The function DigitSum() is designed to return the sum of the digits of an integer.
# For Example if DigitSum(123) is called, the function extracts the rightmost digit, which is 3,
# and adds it to the result of calling DigitSum(12). When DigitSum(12) is called,
# the function extracts the rightmost digit, which is 2,
# and adds it to the result of calling DigitSum(1).
# When DigitSum(1) is called, the function extracts the rightmost digit,
# which is 1, and adds it to the result of calling DigitSum(0).
# When DigitSum(0) is called, the function returns 0, which is the base case. The final result is therefore 1 + 2 + 3 = 6.


def DigitSum(integer):
    if integer == 0:
        return 0
    n = (integer % 10)
    integer = integer // 10
    sum = DigitSum(integer)
    return n + sum

N = int(input())
print(DigitSum(N))
    
