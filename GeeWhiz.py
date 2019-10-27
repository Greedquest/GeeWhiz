from DataCollation.SemanticOutputMap import SemanticMap
import random
import threading
from ImageProcessing import update_so_values, get_so_list
from E3.Fault_Conditions import ConditionCheck as check_for_error

oldValues = {}

def generateDummyValues(dummyMap):
    pass

class Runner:
    def __init__(self, dummyRun=True):
        self._useDummyData = dummyRun
        if dummyRun:
            self.refreshDelay = 3000; 
        self.conditionMaps = []

    def Run(self):
        ###Get user input - get all the calibrations and initialisations
        # define scope
        self.generateOutputMapping(self._useDummyData)
        self.defineDatabaseConnection()
        self.setFaultConditions()

        ### Update loop
        while True:
            self.updateValues()
            self.writeToDatabase()
            # check against error thresholds
            # if error then display alert
            threading.thread.sleep(self.refreshDelay)
            break

        print("Done!")
        print(self.semanticMap)

    def generateOutputMapping(self, useDummyData=True):
        "Generate the mapping between Semantic objects and their ids"
        # do all the b1 b2 stuff here
        #get a list of semantic objects to pass
        self.semanticMap = SemanticMap(None if useDummyData else get_so_list('samplepic_cropped.png'))
        
    def updateValues(self):
        #read new values
        generateDummyValues(self.semanticMap)

    def defineDatabaseConnection(self):
        pass

    def setFaultConditions(self):
        #generate condition map
        pass

    def sendEmail(self):
        pass
    
    def writeToDatabase(self):
        pass

if __name__ == "__main__":
    runner = Runner(True)
    runner.Run()
