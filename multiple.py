class Akhilesh:
    back="oracle db & java"
    def backend(self):
        print("backend implemnentation using",self.back)
class Ankush:
    front="html css and javascript"
    def frontend(self):
        print("frontend implemeting using",self.front)
class TeamLead(Akhilesh,Ankush):
    def show(self):
        print("dynamic website")

a=TeamLead()
a.frontend()
a.backend()
a.show()