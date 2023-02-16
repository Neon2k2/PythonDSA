#Geometric sum:
#1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k)

#Input format : Integer k
#Output format : Geometric sum (upto 5 decimal places)

m = int(input())

def GeoSum(k):
    
#base case
    if k == 0:
        return 1
#induction assume
    ans = GeoSum(k-1)
#induction step
    return 1/(2)**k + ans


result = GeoSum(m)
print("{:.5f}".format(result))