'''
class person_:
    def __init__(self,name,surname,emailid,year_of_birth):
      self.name = name
      self.surname = surname
      self.emailid = emailid
      self.year_of_birth=year_of_birth
nimmy_var=person_("nimmy","joy","nimmy@gmail.com",1990)
print(nimmy_var.name)
print(nimmy_var.surname)
print(nimmy_var.emailid)
'''

class person_:
    def __init__(self,name,surname,emailid,year_of_birth):
      self.name = name
      self.surname = surname
      self.emailid = emailid
      self.year_of_birth=year_of_birth
nimmy_var=person_("nimmy","joy","nimmy@gmail.com",1990)
aibel=person_("aibel","geoge","nimmy@gmail.com",2022)
print(nimmy_var.name)
print(aibel.name)
print(aibel.emailid)
print(type(aibel.name))