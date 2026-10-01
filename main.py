class User:
    # property 
    firstName = ""
    lastname = ""
    age = ""
    
    def __init__(self , firstName , lastname ):
        self.firstName = firstName
        self.lastname = lastname
    def set_age(self , age):
            self.age = age


p1 = User("ali" , "mohammadi")
p1.set_age(18)
print(p1.age)