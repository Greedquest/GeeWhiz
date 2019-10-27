from DataCollation.SemanticOutputMap import SemanticMap
from DataCollation.Semantic_Class import Discrete, 
import random
import threading
oldValues = {}

def generateDummyValues(dummyMap):
    #for outputID,semanticObject in dummyMap:
     #   if type(semanticObject) = 

class Runner:
    def __init__(self, dummyRun=True):
        self._useDummyData = dummyRun
        if dummyRun:
            self.refreshDelay = 3000; 

    def Run(self):
        ###Get user input - get all the calibrations and initialisations
        # define scope
        self.generateOutputMapping(self._useDummyData)
        self.defineDatabaseConnection()
        self.setFaultConditions()

        ### Update loop
        while True:
            self.updateValues()
            # Add to database
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
        self.semanticMap = (
            SemanticMap()
        )  # SemanticMap(None if useDummyData else getMappingData)
        
    def updateValues(self):
        #read new values
        generateDummyValues(self.semanticMap)
        

    def defineDatabaseConnection(self):
        pass

    def setFaultConditions(self):
        pass

    def sendEmail(self):
        

if __name__ == "__main__":
    runner = Runner(True)
    runner.Run()
