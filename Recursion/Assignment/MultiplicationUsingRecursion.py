# Given two integers M & N, calculate and return their multiplication using recursion.
# You can only use subtraction and addition for your calculation. No other operators are allowed.

# Input format :
# Line 1 : Integer M
# Line 2 : Integer N
# Output format :
# M x N


def multiply(m, n):
    if m == 0 or n == 0:
        return 0
    if m < n:
        return n + multiply(m - 1, n)
    else:
        return m + multiply(m, n - 1)

M = int(input())
N = int(input())

result = MultiRec(M,N)
print(result)
