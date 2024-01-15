
class Person:
  def __init__(self, fname, lname = "Joy"):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Man(Person):
  def __init__(self,fn,ln = "Josten",age=100):
    super().__init__(fn,ln)
    self.age = age


x = Person("John")
x.printname()

john = Man("Malcon","Melmorn",18)

john.printname()
print(john.age)


  