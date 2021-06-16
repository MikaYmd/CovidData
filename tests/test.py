import unittest
import Dto
import View
from Model import CovidData
from RecordSubClass import RecordSubClass


class TestCase(unittest.TestCase):
    def test_createRecord(self):
        """This test case checks if the newCovidData is successfully added into list"""
        viewObj = View.View()
        message = "Test failed: data is not added to the array."
        newCovidData = viewObj.controller.createNewObj()
        viewObj.dto.getRecord().append(newCovidData)
        self.assertEqual(viewObj.dto.getRecord()[0], newCovidData, message)


    def test_super_and_sub(self):
        """This test case checks if the data column name “pruid” will be changed or overridden
        when I pass the same junk data “test” to both of CovidData (super class) and RecordSubClass (sub class)."""
        dtoObj = Dto.DTO()
        dtoObj.record.append(CovidData("test", "test", "test", "test", "test", "test", "test", "test", "test",
                                       "test"))  # it'll not change value(name)
        dtoObj.record.append(
            RecordSubClass("test", "test", "test", "test", "test", "test", "test", "test", "test",
                           "test"))  # it'll change value(name)
        self.assertEqual("pruid", dtoObj.getRecord()[0].getPruid(), "Test failed: The name changed.")
        self.assertEqual("test", dtoObj.record[1].getPruid(), "Test failed: The name wasn't overridden.")


if __name__ == '__main__':
    unittest.main()
