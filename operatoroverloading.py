class Addno:
    def __init__(self,num1):
        self.num1=num1

    def __gt__(self,ref):
        if(self.num1==ref.num1):
            return False
        else:
            return True
            

a1=Addno(10)
a2=Addno(10)
a1>a2