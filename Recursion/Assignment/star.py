# Given a string S,compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".

def pairStar(a):
    if len(a) == 0:
        return
    if len(a) == 1:
        return a
    if a[0] == a[1]:
        return a[0] + '*' + pairStar(a[1:])
    else:
        return a[0] + pairStar(a[1:])

string = input()
print(pairStar(string))
