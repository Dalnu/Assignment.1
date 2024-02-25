# Dana Ahmed Alnuaimi ( 202203220 )
from enum import Enum  # Importing the Enum class from the enum module

class Classofservice(Enum):  # Defining a class named Classofservice which inherits from Enum
    Fclass = "FIRST CLASS"  # Enum member Fclass with value "FIRST CLASS"
    Bclass = "BUSINESS CLASS"  # Enum member Bclass with value "BUSINESS CLASS"
    Eclass = "ECONOMY CLASS"  # Enum member Eclass with value "ECONOMY CLASS"
    Pclass = "PREMIUM ECONOMY CLASS"  # Enum member Pclass with value "PREMIUM ECONOMY CLASS"
    Other = "OTHER"  # Enum member Other with value "OTHER"

class Passenger:  # Defining a class named Passenger
    def __init__(self, firstname, lastname, ticketnumber, flyernumber, passportnumber):  # Constructor method with parameters
        self.__firstname = firstname  # Private attribute for first name
        self.__lastname = lastname  # Private attribute for last name
        self.__ticketnumber = ticketnumber  # Private attribute for ticket number
        self.__flyernumber = flyernumber  # Private attribute for flyer number
        self.__passportnumber = passportnumber  # Private attribute for passport number

    # Setter & Getter for the attributes of class 'Passenger':
    def get_firstname(self):  # Method to get the value of the firstname attribute
        return self.__firstname
    def set_firstname(self, firstname):  # Method to set the value of the firstname attribute
        self.__firstname = firstname

    def get_lastname(self):  # Method to get the value of the lastname attribute
        return self.__lastname
    def set_lastname(self, lastname):  # Method to set the value of the lastname attribute
        self.__lastname = lastname

    def get_ticketnumber(self):  # Method to get the value of the ticketnumber attribute
        return self.__ticketnumber
    def set_ticketnumber(self, ticketnumber):  # Method to set the value of the ticketnumber attribute
        self.__ticketnumber = ticketnumber

    def get_flyernumber(self):  # Method to get the value of the flyernumber attribute
        return self.__flyernumber
    def set_flyernumber(self, flyernumber):  # Method to set the value of the flyernumber attribute
        self.__flyernumber = flyernumber

    def get_passportnumber(self):  # Method to get the value of the passportnumber attribute
        return self.__passportnumber
    def set_passportnumber(self, passportnumber):  # Method to set the value of the passportnumber attribute
        self.__passportnumber = passportnumber

    def purchaseticket(self):  # Method to purchase a ticket
        pass  # Placeholder, actual implementation to be added

    def updatepassportinfro(self):  # Method to update passport information
        pass  # Placeholder, actual implementation to be added

class Flight:  # Defining a class named Flight
    def __init__(self, flightnumber, departuredate, departuretime, arrivaltime, gatenumber, terminal):  # Constructor method with parameters
        self.__flightnumber = flightnumber  # Private attribute for flight number
        self.__departuredate = departuredate  # Private attribute for departure date
        self.__departuretime = departuretime  # Private attribute for departure time
        self.__arrivaltime = arrivaltime  # Private attribute for arrival time
        self.__gatenumber = gatenumber  # Private attribute for gate number
        self.__terminal = terminal  # Private attribute for terminal

    # Setter & Getter for the attributes of class 'Flight':
    def get_flightnumber(self):  # Defines a method to get the flight number attribute
        return self.__flightnumber
    def set_flightnumber(self, flightnumber):  # Defines a method to set the flight number attribute
        self.__flightnumber = flightnumber

    def get_departuredate(self):  # Defines a method to get the departure date attribute
        return self.__departuredate
    def set_departuredate(self, departuredate):  # Defines a method to set the departure date attribute
        self.__departuredate = departuredate

    def get_departuretime(self):  # Defines a method to get the departure time attribute
        return self.__departuretime
    def set_departuretime(self, departuretime):  # Defines a method to set the departure time attribute
        self.__departuretime = departuretime

    def get_arrivaltime(self):  # Defines a method to get the arrival time attribute
        return self.__arrivaltime
    def set_arrivaltime(self, arrivaltime):  # Defines a method to set the arrival time attribute
        self.__arrivaltime = arrivaltime

    def get_gatenumber(self):  # Defines a method to get the gate number attribute
        return self.__gatenumber
    def set_gatenumber(self, gatenumber):  # Defines a method to set the gate number attribute
        self.__gatenumber = gatenumber

    def get_terminal(self):  # Defines a method to get the terminal attribute
        return self.__terminal
    def set_terminal(self, terminal):  # Defines a method to set the terminal attribute
        self.__terminal = terminal

    def checkinpassenger(self):  # Method to check in a passenger
        pass  # Placeholder, actual implementation to be added

    def flightduration(self):  # Method to calculate flight duration
        pass  # Placeholder, actual implementation to be added

class BoardingPass(Passenger):  # Defining a class named BoardingPass which inherits from Passenger
    def __init__(self, firstname, lastname, ticketnumber, flyernumber, passportnumber, flight, seat, boardingtime):  # Constructor method with parameters
        super().__init__(firstname, lastname, ticketnumber, flyernumber, passportnumber)  # Calling the constructor of the superclass
        self._flight = flight  # Protected attribute for flight
        self._seat = seat  # Protected attribute for seat
        self._boardingtime = boardingtime  # Protected attribute for boarding time

    # Setter & Getter for the attributes of class 'BoardingPass':
    def get_flight(self):  # Defines a method to get the flight associated with the boarding pass.
        return self._flight
    def set_flight(self, flight):  # Defines a method to set the flight associated with the boarding pass.
        self._flight = flight


    def get_seat(self):  # Defines a method to get the seat associated with the boarding pass.
        return self._seat
    def set_seat(self, seat):  # Defines a method to set the seat associated with the boarding pass.
        self._seat = seat

    def get_boardingtime(self):  # Defines a method to get the boarding time associated with the boarding pass.
        return self._boardingtime
    def set_boardingtime(self, boardingtime):  # Defines a method to set the boarding time associated with the boarding pass.
        self._boardingtime = boardingtime


    def printboardingpass(self):  # Defines a method to print the boarding pass details.
        print("Boarding Pass".center(50, "-"))  # Prints the title "Boarding Pass" centered with dashes.
        print(f"Passenger Name: {self.get_firstname()} {self.get_lastname()}")  # Prints passenger name.
        print(f"Departure Airport: {self._flight.get_departuredate()}")  # Prints departure date.
        print(f"Destination Airport: {self._flight.get_arrivaltime()}")  # Prints arrival time.
        print(f"Flight Number: {self._flight.get_flightnumber()}")  # Prints flight number.
        print(f"Date of Departure: {self._flight.get_departuredate()}")  # Prints departure date.
        print(f"Departure Time: {self._flight.get_departuretime()}")  # Prints departure time.
        print(f"Gate: {self._flight.get_gatenumber()}")  # Prints gate number.
        print(f"Boarding Time: {self._boardingtime}")  # Prints boarding time.
        print(f"Seat: {self._seat}")  # Prints seat number.
        print(f"Arrival Time: {self._flight.get_arrivaltime()}")  # Prints arrival time.
        print(f"Terminal: {self._flight.get_terminal()}")  # Prints terminal number.
        print("".center(50, "-"))  # Prints dashes to separate the boarding pass.


    def updateboardingtime(self):  # Method to update boarding time
        pass  # Placeholder, actual implementation to be added

class Airline:  # Defining a class named Airline
    def __init__(self, name, boardingpasstext, classofservice, reminder, referencecode):  # Constructor method with parameters
        self._name = name  # Protected attribute for airline name
        self._boardingpasstext = boardingpasstext  # Protected attribute for boarding pass text
        self._classofservice = classofservice  # Protected attribute for class of service
        self._reminder = reminder  # Protected attribute for reminder
        self._referencecode = referencecode  # Protected attribute for reference code

    # Setter & Getter for the attributes of class 'Airline':
    def get_name(self):  # Defines a method to get the name associated with the boarding pass.
        return self._name
    def set_name(self, name):  # Defines a method to set the name associated with the boarding pass.
        self._name = name

    def get_boardingpasstext(self):  # Defines a method to get the boarding pass text.
        return self._boardingpasstext
    def set_boardingpasstext(self, boardingpasstext):  # Defines a method to set the boarding pass text.
        self._boardingpasstext = boardingpasstext

    def get_classofservice(self):  # Defines a method to get the class of service associated with the boarding pass.
        return self._classofservice
    def set_classofservice(self, classofservice):  # Defines a method to set the class of service associated with the boarding pass.
        self._classofservice = classofservice

    def get_reminder(self):  # Defines a method to get the reminder associated with the boarding pass.
        return self._reminder
    def set_reminder(self, reminder):  # Defines a method to set the reminder associated with the boarding pass.
        self._reminder = reminder

    def get_referencecode(self):  # Defines a method to get the reference code associated with the boarding pass.
        return self._referencecode
    def set_referencecode(self, referencecode):  # Defines a method to set the reference code associated with the boarding pass.
        self._referencecode = referencecode


    def issueboardingpass(self):  # Method to issue a boarding pass
        pass  # Placeholder, actual implementation to be added

    def report(self):  # Method to generate a report
        pass  # Placeholder, actual implementation to be added


# Create an object:

# Creating an instance of the Airline class
airline = Airline(name = "NATIONAL AIRLINES", boardingpasstext = "FIRST CLASS", classofservice = Classofservice.Fclass,
                  reminder = "PLEASE BE AT THE GATE AT BOARDING TIME.", referencecode = "5A6BCD78")

# Creating an instance of the Passenger class
passenger = Passenger(firstname = "JAMES", lastname = "SMITH", ticketnumber = "629", flyernumber = "1234", passportnumber = "12345678")

# Creating an instance of the Flight class
flight = Flight(flightnumber="NA4321", departuredate="06 DEC 20", departuretime="11:40", arrivaltime="13:30",
                gatenumber="03", terminal="2")

# Creating an instance of the BoardingPass class
boarding_pass = BoardingPass(firstname="JAMES", lastname="SMITH", ticketnumber="629", flyernumber="", passportnumber="",
                              flight=flight, seat="09A", boardingtime="11:20")

# Displaying Airline details
print("Airline Name:", airline.get_name())
print("Class of Service:", airline.get_classofservice())
print("Reference Code:", airline.get_referencecode())
print("Reminder:", airline.get_reminder())

# Displaying Passenger details
print("Passenger Name:", passenger.get_firstname(), passenger.get_lastname())
print("Ticket Number:", passenger.get_ticketnumber())

# Displaying Flight details
print("Flight Number:", flight.get_flightnumber())
print("Departure Date:", flight.get_departuredate())
print("Departure Time:", flight.get_departuretime())
print("Arrival Time:", flight.get_arrivaltime())
print("Gate:", flight.get_gatenumber())
print("Terminal:", flight.get_terminal())

# Displaying Boarding Pass details
boarding_pass.printboardingpass()

