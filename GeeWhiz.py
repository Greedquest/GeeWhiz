from DataCollation.SemanticOutputMap import SemanticMap
from time import sleep
from ImageProcessing import update_so_values, get_so_list
from E3.Fault_Conditions import ConditionCheck as check_for_error
from Email import dispatchFaultMessage
from camCapture import camCapture


oldValues = {}

class Runner:
    def __init__(self, dummyRun=True):
        self._useDummyData = dummyRun
        if dummyRun:
            self.refreshDelay = 2.4
            # seconds
        self.imagePath = "samplepic.png"

    def Run(self):
        ###Get user input - get all the calibrations and initialisations
        # define scope
        camCapture(self.imagePath)
        self.generateOutputMapping()
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
                
            camCapture(self.imagePath)

        print("Done!")
        print(self.semanticMap)
        
    def defineDatabaseConnection(self):
        define_log(self.semanticMap.values())

    def writeToDatabase(self):
        write_to_log(self.semanticMap.values())

    def generateOutputMapping(self):
        "Generate the mapping between Semantic objects and their ids"
        # do all the b1 b2 stuff here
        # get a list of semantic objects to pass
        self.semanticMap = SemanticMap(
            None if self._useDummyData else get_so_list("samplepic_cropped.png")
        )

    def updateValues(self):
        # read new values

        update_so_values(self.semanticMap.values(), self.imagePath)



    def setFaultConditions(self):
        # generate condition maps
        self.conditionMaps = []
        pass

    def checkForErrors(self):
        for conditionMap in self.conditionMaps:
            if check_for_error(conditionMap, self.semanticMap):
                # send error alert
                dispatchFaultMessage(conditionMap, self.semanticMap)
                anyError = True

        return anyError


if __name__ == "__main__":
    runner = Runner(True)
    runner.Run()
