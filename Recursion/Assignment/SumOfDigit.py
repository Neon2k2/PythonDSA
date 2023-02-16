def DigitSum(integer):
    if integer == 0:
        return 0
    n = (integer % 10)
    integer = integer // 10
    sum = DigitSum(integer)
    return n + sum

N = int(input())
print(DigitSum(N))
    
