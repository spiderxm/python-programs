class info():
 def __init__(self,name,clas,rollno):
    self.name=name
    self.clas=clas
    self.rollno=rollno
 def showinfo(self):
   print("name is {},class is {},roll no is {}".format(self.name,self.clas,self.rollno))

class student(info):
    def __init__(self,name,clas,rollno,age):
        info.__init__(self,name,clas,rollno)
        self.age=age

    def show(self):
        info.showinfo(self)
        print("Age is {}".format(self.age))



a=student("mrigank","College 1st year",192222,18)
a.show()
