from DataCollation.SemanticOutputMap import SemanticMap
from time import sleep
from ImageProcessing import update_so_values, get_so_list
from E3.Fault_Conditions import ConditionCheck as check_for_error
from Email import dispatchFaultMessage

oldValues = {}

def generateDummyValues(dummyMap):
    pass

class Runner:
    def __init__(self, dummyRun=True):
        self._useDummyData = dummyRun
        if dummyRun:
            self.refreshDelay = 2.4; #seconds
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
            if self.checkForErrors():
                break
            else:
                sleep(self.refreshDelay)

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
    
    def checkForErrors(self):
        for conditionMap in self.conditionMaps:
            if check_for_error(conditionMap, self.semanticMap):
                #send error alert
                dispatchFaultMessage(conditionMap,self.semanticMap)
                anyError = True
                
        return anyError

    
    def writeToDatabase(self):
        pass

if __name__ == "__main__":
    runner = Runner(True)
    runner.Run()
