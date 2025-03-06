class Father:
    surname="verma"
    def show (self):
        print("my surnme is",self.surname)
class Son1(Father):
    def sho(self):
        print("Ankit",self.surname)
class Son2(Father):
    def so(self):
        print("ankush",self.surname)

s1=Son1()
s2=Son2()
 
s1.sho()
s2.so()