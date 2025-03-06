class A:
    num1=int(input("enter the 1st no"))
    num2=int(input("enter the 1st no"))

    def add(self):
        print("addition: ",self.num1+self.num2)
    def sub(self):
        print("subtraction ",self.num1-self.num2)

class B(A):

    def multi(self):
        print("multiplication: ",self.num1*self.num2)
    def div(self):
        print("divison ",self.num1/self.num2)


obj=B()
obj.add()
obj.sub()
obj.multi()
obj.div()