'''class person_:
    def __init__(xyz,name1,surname,emailid,year_of_birth):
      xyz.name1 = name #rhs should be same as init variable name
      xyz.surname = surname
      xyz.emailid = emailid
      xyz.year_of_birth=year_of_birth
nimmy_var=person_("nimmy","joy","nimmy@gmail.com",1990)
aibel=person_("aibel","geoge","nimmy@gmail.com",2022)
print(nimmy_var.name)
print(aibel.name)
print(aibel.emailid)
print(type(aibel.name))
print(aibel.name+" "+aibel.surname)'''
class person_:
    def __init__(xyz,name1,surname,emailid,year_of_birth):
      xyz.name = name1
      xyz.surname = surname
      xyz.emailid = emailid
      xyz.year_of_birth=year_of_birth

    def age(xyz,current_year):
        return current_year-xyz.year_of_birth
nimmy_var=person_("nimmy","joy","nimmy@gmail.com",1990)
aibel=person_("aibel","geoge","nimmy@gmail.com",2022)
print(nimmy_var.name)
print(aibel.name)
print(aibel.emailid)
print(type(aibel.name))
print(aibel.name+" "+aibel.surname)
print(aibel.age(2023))
#if we provide multiple init fns, it will take latest one

