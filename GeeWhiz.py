from DataCollation.SemanticOutputMap import SemanticMap
from DataCollation.Semantic_Class import Discrete, 
import random
oldValues = {}

def generateDummyValues(dummyMap):
    for outputID,semanticObject in dummyMap:
        if type(semanticObject) = 

class Runner:
    def __init__(self, dummyRun=True):
        self._useDummyData = dummyRun

    def Run(self):
        ###Get user input
        self.generateOutputMapping(self._useDummyData)
        self.defineDatabaseConnection()
        self.setFaultConditions()

        ### Update loop
        while True:
            self.updateValues()
            # Add to database
            # check against error thresholds
            # if error then display alert
            break

        print("Done!")
        print(self.semanticMap)

    def generateOutputMapping(self, useDummyData=True):
        "Generate the mapping between Semantic objects and their ids"
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
