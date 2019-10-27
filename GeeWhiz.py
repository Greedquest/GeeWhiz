import sys
import os
from pathlib import Path
currentFile = Path(os.path.realpath(__file__))
sys.path.append(str(currentFile.parent))
sys.path.append(str(currentFile.parent / "DataCollation"))

from SemanticOutputMap import SemanticMap
from database import define_log, write_to_log
from time import sleep
from ImageProcessing import update_so_values, get_so_list
from E3.Fault_Conditions import ConditionCheck as check_for_error
from Email import dispatchFaultMessage
from camCapture import camCapture
import cv2
import random


class App:
    def __init__(self, dummyRun=False):
        self._useDummyData = dummyRun
        if dummyRun:
            self.refreshDelay = 2.4
            # seconds
        self.imagePath = "newimage.png"

    def Run(self):
        ###Get user input - get all the calibrations and initialisations
        # define scope
        self.updateImage()
        self.generateOutputMapping()
        self.defineDatabaseConnection()
        self.setFaultConditions()

        ### Update loop
        while True:
            print(self.semanticMap)
            self.updateValues()
            self.writeToDatabase()
            if self.checkForErrors():
                break
            else:
                sleep(self.refreshDelay)

            self.updateImage()

        print("Done!")

    def updateImage(self):
        print("Snap")
        self.imagePath = "samplepic_cropped.png"
        #camCapture(self.imagePath)
        self.chickenpic = cv2.imread(self.imagePath,1)
        
    def defineDatabaseConnection(self):
        define_log(self.semanticMap.values())

    def writeToDatabase(self):
        write_to_log(self.semanticMap.values())

    def generateOutputMapping(self):
        "Generate the mapping between Semantic objects and their ids"
        # do all the b1 b2 stuff here
        # get a list of semantic objects to pass
        so_list = get_so_list(self.chickenpic)
        print(so_list)
        self.semanticMap = SemanticMap({objectIndex:semanticObject for objectIndex,semanticObject in enumerate(so_list)})

    def updateValues(self):
        # read new values

        update_so_values(self.semanticMap.values(), self.chickenpic)
        #for i in self.semanticMap.values():
        #    i.value = random.randint(1,9)

    def setFaultConditions(self):
        # generate condition maps
        self.conditionMaps = []
        pass

    def checkForErrors(self):
        anyError = False
        for conditionMap in self.conditionMaps:
            if check_for_error(conditionMap, self.semanticMap):
                # send error alert
                dispatchFaultMessage(conditionMap, self.semanticMap)
                anyError = True

        return anyError


if __name__ == "__main__":

    geeWhizApp = App(True)
    geeWhizApp.Run()
