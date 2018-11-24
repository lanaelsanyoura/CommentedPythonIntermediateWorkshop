from datetime import date, datetime #for date

class Person:
    """
    A person class

    ==== Attributes ====
    firstname: str
    lastname: str
    birthdate: date YEAR, MONTH, DAY
    address: str
    """
    def __init__(self): #, firstname, lastname, birthdate, address):
        #self.firstname = firstname
        #self.lastname = lastname
        #self.birthdate = birthdate
        #self.address = address

    def __str__(self):
        """
        Return the string in a human-readable manner
        @return: string
        """
        #return "{} {}".format(self.firstname, self.lastname)

    def age(self):
        """
        Given the current date, return the age of this person
        :return: int age
        """
        #today = date.today()
        #age = today.year - self.birthdate.year
        #if today < date(today.year, self.birthdate.month, self.birthdate.day):
        #    age -= 1

        #return age
        pass

    def getInfo(self):
        """
        Return the information of this user to showcase overriding
        :return:
        """
        #print("I am a generic person")
        pass

# Example Build
#person = Person("Joane", "Do", date(1997, 4, 20), "50 st george str")

