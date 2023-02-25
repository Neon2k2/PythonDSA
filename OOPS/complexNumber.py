class ComplexNumbers:
    def __init__(self, L1, L2, choice):
        self.L1 = L1
        self.L2 = L2
        self.choice = choice

    def Plus(self):
        real_ = self.L1[0] + self.L2[0]
        complex_ = self.L1[1] + self.L2[1]
        return "{} + i{}".format(real_, complex_)

    def Multiply(self):
        real_ = self.L1[0]*self.L2[0] - self.L1[1]*self.L2[1]
        complex_ = self.L1[0]*self.L2[1] + self.L1[1] * self.L2[0]
        return "{} + i{}".format(real_, complex_)

    def Print(self):
        if self.choice == 1:
            print(self.Plus())
        elif self.choice == 2:
            print(self.Multiply())
        

# Driver's code goes here.

L1 = [int(x) for x in input().split()]
L2 = [int(x) for x in input().split()]
choice = int(input())

obj = ComplexNumbers(L1, L2, choice)
obj.Print()


# input: 
# 10 15
# 12 40
# 1

# output:
# 22 + i55
