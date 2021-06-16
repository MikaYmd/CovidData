import Controller
import Dto


class View:
    # Object
    dto = Dto.DTO()  # filename.classname
    controller = Controller.Controller()

    def displayMenu(self):
        """This method is to display menu. It keep displaying menu
            until user select “7” to exit."""
        i = 0
        while i != 8:
            i = self.controller.menuInput("\nChoose an option "
                                          "\n1. Reload the data. "
                                          "\n2. Write to a new file "
                                          "\n3. Display records "
                                          "\n4. Create a new record "
                                          "\n5. Edit a record "
                                          "\n6. Delete a record"
                                          "\n7. Display a new file with graph "
                                          "\n8. Exit")

            if i == 1:
                self.reloadData()

            elif i == 2:
                self.writeToFile()

            elif i == 3:
                self.displayRecord()

            elif i == 4:
                self.createRecord()

            elif i == 5:
                self.editRecord()

            elif i == 6:
                self.deleteRecord()

            elif i == 7:
                self.displayGraph()


    def reloadData(self):
        """This method reloads data and display message that Record reloaded."""
        self.dto.readFromData()
        print("Record reloaded.")

    def displayRecord(self):
        """This method asks to user how many record does user want to see, and displays data
           according to user input. It will notify user if user typed out of range number."""
        counter = 0
        selectedData = self.controller.chooseRecord("Enter how many records you want to display: ")
        if selectedData != 0 and len(self.dto.getRecord()) >= selectedData >= 0:
            for line in self.dto.getRecord():
                print(line.__dict__)  # cast the object to dictionary
                counter = counter + 1
                if counter == selectedData:
                    break
        else:
            print("Please choose number within the number of records.")

    def deleteRecord(self):
        """This method asks user which record to delete, and it deletes data based on user input number.
           It will notify user if user typed out of range number."""
        selectedData = self.controller.chooseRecord("Enter the record number: ") - 1
        if selectedData >= (len(self.dto.getRecord())):
            print("Please choose number within the number of records.")
        else:
            print(self.dto.getRecord()[selectedData].__dict__)
            if self.controller.confirmMsg("Do you want to delete this data? (y/n): ") == "y":
                self.dto.getRecord().remove(self.dto.getRecord()[selectedData])
                print("Record deleted.")

    def editRecord(self):
        """This method asks user which record to delete, and it deletes data based on user input number.
           It will notify user if user typed out of range number."""
        selectedData = self.controller.chooseRecord("Enter the record number: ") - 1
        print(self.dto.getRecord()[selectedData].__dict__)
        if self.controller.confirmMsg("Do you want to edit this data? (y/n): ") == "y":
            self.controller.modifyData(self.dto.getRecord()[selectedData])
            print("Record edited.")

    def createRecord(self):
        """This method create a new record based on user input, and store it in the record list."""
        self.dto.getRecord().append(self.controller.createNewObj())
        print("Record added.")

    def writeToFile(self):
        """This method connects to dto.writeToCsv() to write the record into newCSV file."""
        self.dto.writeToCsv()
        print("File written.")

    def displayGraph(self):
        """This method connrcts to dto.displayVerticalGraph() to display the vertical bar graph"""
        self.dto.displayVerticalGraph()
        print("Vertical Bar Graph displayed.")









