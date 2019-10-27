class info:
 def __init__(self,name,clas,rollno):
    self.name=name
    self.clas=clas
    self.rollno=rollno
 def showinfo(self):
   print("name is {},class is {},roll no is {}".format(self.name,self.clas,self.rollno))





a=info("mrigank","college first year",195516)
a.showinfo()

