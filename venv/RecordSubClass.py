from Model import CovidData

class RecordSubClass(CovidData):
    """This class is subclass of Model.py"""

    def __init__(self, pruid, prname, prnameFR, date, numconf, numprob, numdeaths, numtotal, numtoday, ratetotal):
        """Variables to create the object (RecordSubClass)

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
        self.pruid = pruid
        self.prname = prname
        self.prnameFR = prnameFR
        self.date = date
        self.numconf = numconf
        self.numprob = numprob
        self.numdeaths = numdeaths
        self.numtotal = numtotal
        self.numtoday = numtoday
        self.ratetotal = ratetotal