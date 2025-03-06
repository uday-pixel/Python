class Father:
    surname="verma"
class Son(Father):
    def show(self):
        print("akash",self.surname)
class Gson(Son):
    def sho(self):
        print("ankit",self.surname)
    
a=Son()
a.show()

b=Gson()
b.sho()
b.show()