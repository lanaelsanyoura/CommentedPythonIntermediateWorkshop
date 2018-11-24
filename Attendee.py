from Person import Person

class Attendee(Person):
    """
    An Attendee Class that can sign up to and cancel workshops

    ==== Attributes ====
    firstname: str
    lastname: str
    birthdate: date, YEAR, MONTH, DAY
    address: str
    email: str
    workshops: list[Workshops]
    """

    def __init__(self): #, firstname, lastname, birthdate, address, email):
        #super().__init__(firstname, lastname, birthdate, address)
        #self.email = email
        #self.workshops = []
        pass

    def sign_up(self, workshop):
        """
        Add a workshop to our list
        @param workshop: Workshop we are attending
        @return: True if there is no conflict, False otherwise
        """
        # Check that this workshop doesn't conflict with any other
        #for ws in self.workshops:
        #    if workshop.conflicts(ws):
        #        print("This workshop conflicts with {}".format(ws.title))
        #        return False
        #self.workshops.append(workshop)
        #return True
        pass

    def cancel(self, workshop):
        """
        Remove the workshop from our list, and remove ourselves from their list
        @param workshop: Workshop instance
        @return: Nothing
        """
        #self.workshops.remove(workshop)
        #workshop.attendees.remove(self)
        pass

    def __str__(self):
        """
        Return the string of the name of this attendee and all the workshops
        they are attending
        @return: string
        """
        #return "{} : {}".format(super().__str__() , [ws.title for ws in self.workshops])
        pass

    def getInfo(self):
        """
        Return the information of this user to showcase overriding
        :return:
        """
        #print("I am an attendee")
        pass

# Example Build
# attendee = Attendee("Lana", "Sanyoura", date(1997, 10, 23), "223", "lsa@gmail.com")