from RecordSubClass import RecordSubClass

class Controller:

    def menuInput(self, message):
        """This method asks user to choose the number from the menu."""
        return int(input(message))

    def chooseRecord(self, message): #Enter the record number
        """This method asks user to enter the record number"""
        return int(input(message))

    def confirmMsg(self, message):
        """This method asks user confirmation and enter yes or no (y/n)."""
        return input(message)

    def modifyData(self, data):
        """This method asks user to enter the info to edit the data."""
        data.setPruid(input("Edit Pruid: "))
        data.setPrname(input("Edit Prname: "))
        data.setPrnameFR(input("Edit PrnameFR: "))
        data.setDate(input("Edit Date: "))
        data.setNumconf(input("Edit Numconf: "))
        data.setNumprob(input("Edit Numprob: "))
        data.setNumdeaths(input("Edit Numdeaths: "))
        data.setNumtotal(input("Edit Numtotal: "))
        data.setNumtoday(input("Edit Numtoday: "))
        data.setRatetotal(input("Edit Ratetotal: "))

    def createNewObj(self):
        """This method asks user to enter the info to create the data.
        Using record object from sub class (RecordSubClass)"""
        data = RecordSubClass("", "", "", "", "", "", "", "", "", "")
        data.setPruid(input("Enter Pruid: "))
        data.setPrname(input("Enter Prname: "))
        data.setPrnameFR(input("Enter PrnameFR: "))
        data.setDate(input("Enter Date: "))
        data.setNumconf(input("Enter Numconf: "))
        data.setNumprob(input("Enter Numprob: "))
        data.setNumdeaths(input("Enter Numdeaths: "))
        data.setNumtotal(input("Enter Numtotal: "))
        data.setNumtoday(input("Enter Numtoday: "))
        data.setRatetotal(input("Enter Ratetotal: "))
        return data