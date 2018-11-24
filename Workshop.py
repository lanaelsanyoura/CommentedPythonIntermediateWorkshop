from datetime import date, datetime, time
#from Person import Person
#from Attendee import Attendee

class Workshop():
    """
    A class that has attendees and workshop details
    @param date String : Day, Month
    @param time str: hour:minutes
    @param duration int:
    """
    def __init__(self, dates, start, end, room, title, description, host, capacity=50):
        self.date = dates
        self.start_time = start
        self.end_time = end
        self.room = room
        self.attendees = []
        self.host = host
        self.description = description
        self.title = title
        self.capacity = capacity

    def conflicts(self, other):
        """
        Conflicts:
               <-------- -------->
        <---- ----> <-->   <---- ---->
        :param other: the workshop we are testing for conflicts against
        :return: True if these two workshops conflict in time
        """
        # return (self.date == other.date) and (self.start_time.time() <= other.start_time.time() <=
        #         self.end_time.time()) or\
        #        (other.start_time.time()
        #         <= self.start_time.time() <= other.end_time.time())

    def add_attendees(self, attendee):
        # if len(self.attendees) < self.capacity and attendee.sign_up(self):
        #     self.attendees.append(attendee)
        #     return True
        # else:
        #     print("Sorry, we have reached max capacity")
        #     return False
        pass

    def __str__(self):
        str = "===== {} ====\n".format(self.title)
        str += self.description + "\n"
        str += "Hosted by: {} \n".format(self.host)
        str += "{}, {} --> {}\n".format(self.date, self.start_time, self.end_time)
        str += "Room {}\n".format(self.room)
        return str

    def get_str_attendees(self):
        # all_attendees = ""
        # for att in self.attendees:
        #     all_attendees += att.firstname + " " + att.lastname + "\n"
        # return all_attendees
        pass

# example build
#title = "Intermediate Python"
#desc = "Spruce up your python skills!"
#ws = Workshop(date(2018, 11, 24), datetime(2018, 11, 24, 12,30),
#              datetime(2018, 11, 24, 3, 30), "BA1190", title, desc, host)
