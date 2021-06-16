import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from RecordSubClass import RecordSubClass


# References
# (DictReader) URL: https://www.foxinfotech.in/2018/09/python-read-csv-columns-into-list.html
# (DictWriter) URL: https://docs.python.org/3/library/csv.html


class DTO:
    """List to store CovidData"""
    record = []

    def readFromData(self):
        try:
            """Open and read CSV file by using DictReader
                so that only selected columns can be displayed"""
            with open('covid19-download.csv', 'r') as f:
                reader = csv.DictReader(f)
                """Loop through the CSV file and get data for the columns below. And then add data into the list
                    Args:
                     data: data which will be stored in the list"""
                counter = 1
                for row in reader:
                    # Using RecordSubClass from subclass of Model.py
                    data = RecordSubClass(row['pruid'], row['prname'], row['prnameFR'], row['date'], row['numconf'],
                                          row['numprob'], row['numdeaths'], row['numtotal'], row['numtoday'],
                                          row['ratetotal'])
                    self.record.append(data)
                    counter = counter + 1
                    if counter == 101:  # to display 100 data
                        break
            """Loop through the CSV file and store the data into record list.
                Args: 
                  line.dict: each line of data which is casted to dictionary."""

        except FileNotFoundError:
            """Exception Handling for FileNotFoundError
                Message will be displayed when program can't find the file."""
            print('This file does not exist. ')

    def getRecord(self):
        """This method is to get the record of list"""
        return self.record

    def writeToCsv(self):
        """This method is to write the list of data to the newCSV file"""
        with open('newCsv.csv', 'w') as csvfile:
            fieldNames = ['pruid', 'prname', 'prnameFR', 'date', 'numconf', 'numprob', 'numdeaths', 'numtotal',
                          'numtoday', 'ratetotal']
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
            writer.writeheader()
            for covidData in self.getRecord():
                writer.writerow({'pruid': covidData.getPruid(), 'prname': covidData.getPrname(),
                                 'prnameFR': covidData.getPrnameFR(),
                                 'date': covidData.getDate(), 'numconf': covidData.getNumconf(),
                                 'numprob': covidData.getNumprob(), 'numdeaths': covidData.getNumdeaths(),
                                 'numtotal': covidData.getNumtotal(), 'numtoday': covidData.getNumtoday(),
                                 'ratetotal': covidData.getRatetotal()})

    def displayVerticalGraph(self):
        """This method is to display vertical bar graph of cases for each province"""
        data = pd.read_csv('newCsv.csv', usecols=['prname'])
        on_data = (data == 'Ontario')
        bc_data = (data == 'British Columbia')
        qc_data = (data == 'Quebec')
        ab_data = (data == 'Alberta')
        sk_data = (data == 'Saskatchewan')
        mb_data = (data == 'Manitoba')
        nb_data = (data == 'New Brunswick')
        nl_data = (data == 'Newfoundland and Labrador')
        ns_data = (data == 'Nova Scotia')
        pe_data = (data == 'Prince Edward Island')
        nt_data = (data == 'Northwest Territories')
        nu_data = (data == 'Nunavut')
        yt_data = (data == 'Yukon')
        tr_data = (data == 'Repatriated travellers')
        other_data = (data == 'Canada')
        on_total = int(on_data.sum())
        bc_total = int(bc_data.sum())
        qc_total = int(qc_data.sum())
        ab_total = int(ab_data.sum())
        sk_total = int(sk_data.sum())
        mb_total = int(mb_data.sum())
        nb_total = int(nb_data.sum())
        nl_total = int(nl_data.sum())
        ns_total = int(ns_data.sum())
        pe_total = int(pe_data.sum())
        nt_total = int(nt_data.sum())
        nu_total = int(nu_data.sum())
        yt_total = int(yt_data.sum())
        tr_total = int(tr_data.sum())
        other_total = int(other_data.sum())

        y = np.array([on_total, bc_total, qc_total, ab_total, sk_total, mb_total, nb_total, nl_total, ns_total, pe_total, nt_total, nu_total, yt_total, tr_total, other_total])
        x = ['ON', 'BC', 'QC', 'AB', 'SK', 'MB', 'NB', 'NL', 'NS', 'PE', 'NT', 'NU', 'YT', 'Travellers', 'Other']
        plt.xticks(rotation=70)
        plt.yticks([0, 5, 10, 15, 20, 25, 30, 35])
        plt.bar(x, height=y, tick_label=x, width=0.4)
        plt.title('Covid cases per province')
        plt.show()

