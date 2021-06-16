class CovidData:
    """This is super class of RecordSubClass.py"""
    def __init__(self):
        """Variables to create the object (CovidData)

         Parameters
         __________
            pruid : id
            prname : province name (English)
            prnameFR : province name (French)
            date : date
            numconf : confirmed number
            numprob : number maight be positive
            numdeath : number of death
            numtotal : number of total
            numtoday : number of today's case
            ratetotal : rate of total
        """
        self.pruid = "pruid"
        self.prname = "prname"
        self.prnameFR = "prnameFR"
        self.date = "date"
        self.numconf = "numconf"
        self.numprob = "numprob"
        self.numdeaths = "numdeaths"
        self.numtotal = "numtotal"
        self.numtoday = "numtoday"
        self.ratetotal = "ratetotal"

    def setPruid(self, pruid):
        """Setter for pruid"""
        self.pruid = pruid

    def getPruid(self):
        """Getter for pruid"""
        return self.pruid

    def setPrname(self, prname):
        """Setter for prname"""
        self.prname = prname

    def getPrname(self):
        """Getter for prname"""
        return self.prname

    def setPrnameFR(self, prnameFR):
        """Setter for prnameFR"""
        self.prnameFR = prnameFR

    def getPrnameFR(self):
        """Getter for prnameFR"""
        return self.prnameFR

    def setDate(self, date):
        """Setter for data"""
        self.date = date

    def getDate(self):
        """Getter for data"""
        return self.date

    def setNumconf(self, numconf):
        """Setter for numconf"""
        self.numconf = numconf

    def getNumconf(self):
        """Getter for numconf"""
        return self.numconf

    def setNumprob(self, numprob):
        """Setter for numprob"""
        self.numprob = numprob

    def getNumprob(self):
        """Getter for numprob"""
        return self.numprob

    def setNumdeaths(self, numdeaths):
        """Setter for numdeaths"""
        self.numdeaths = numdeaths

    def getNumdeaths(self):
        """Getter for numdeaths"""
        return self.numdeaths

    def setNumtotal(self, numtotal):
        """Setter for numtotal"""
        self.numtotal = numtotal

    def getNumtotal(self):
        """Getter for numtotal"""
        return self.numtotal

    def setNumtoday(self, numtoday):
        """Setter for numtoday"""
        self.numtoday = numtoday

    def getNumtoday(self):
        """Getter for numtoday"""
        return self.numtoday

    def setRatetotal(self, ratetotal):
        """Setter for ratetotal"""
        self.ratetotal = ratetotal

    def getRatetotal(self):
        """Getter for ratetotal"""
        return self.ratetotal







