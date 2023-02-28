# implementation fraction class with the following properties and functions.
# properties: numerator and denominator
# function: Parametrized Contructor and Add , Multiply, Simplify and Print
# Input:
# 67 14
# 1
# 2 7 78
# output:
# 67/156



import math

class Fraction:
    #Create your fraction class here.
    def __init__(self, num,den):
        self.num = num
        self.den = den

    def lcm(self, a, b):
        return abs(a*b) // math.gcd(a, b)        
        
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    
    def __add__(self,obj):
        temp = Fraction(self.num,self.den)
        a = self.lcm(self.den,obj.den)
        b = (self.num * (a//self.den)) + (obj.num * (a//obj.den))
        self.num = temp.num = b
        self.den = temp.den = a
        return temp
    
    def __mul__(self,obj):
        temp = Fraction(self.num,self.den)
        a = self.num * obj.num
        b = self.den * obj.den
        self.num = temp.num = a
        self.den = temp.den = b
        return temp
    
    def plus(self,obj):
        return self + obj
    
    def multiply(self,obj):
        return self * obj
    
    def simplify(self):
        a = math.gcd(self.num,self.den)
        self.num //= a
        self.den //= a
        return self
    
    def Print(self):
        print(self)

#Driver code goes here.
num1,den1 = list(map(int,input().split()))
fr1 = Fraction(num1,den1)
reps = int(input())
for _ in range(reps):
    op,num2,den2 = list(map(int,input().split()))
    fr2 = Fraction(num2,den2)
    if op == 1:
        fr1.plus(fr2)
        fr1.simplify()
        fr1.Print()
    elif op == 2:
        fr1.multiply(fr2)
        fr1.simplify()
        fr1.Print()

