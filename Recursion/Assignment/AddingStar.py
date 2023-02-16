string = 'aaaa'

def pairStar(a):
    if len(a) == 0:
        return
    if len(a) == 1:
        return a
    if a[0] == a[1]:
        return a[0] + '*' + pairStar(a[1:])
    else:
        return a[0] + pairStar(a[1:])
    
print(pairStar(string))
# output: 'a*a*a*a'
