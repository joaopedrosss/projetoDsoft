class P:
    def __init__(self,nome):
            self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nomeDado):
        self.__nome = nomeDado

class Student:
    def __init__(self,grade):
         self.__grade = grade
    
    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self,value):
         
        try:
              newGrade = float(value)
        except(TypeError, ValueError) as e:
             raise type(e)("New grade {} is an invalid value".format(str(value)))
        if(value < 0) or (value > 10):
            print("Type a valid value")
            return 
        self.__grade = newGrade
        



elian = P("ELI")    
print(elian.nome)
elian.nome = ("Sandra")
print(elian.nome)

a = Student(7)

print(a.grade)

a.grade = 9

print(a.grade)
