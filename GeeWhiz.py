from DataCollation.SemanticOutputMap import SemanticMap

class Runner:
    def __init__(self, dummyRun=True):
        self._useDummyData = dummyRun
        
    def __repr__(self):
        return "oy"

    def Run(self):
        ###Get user input
        self.generateOutputMapping(self._useDummyData)
        self.defineDatabaseConnection()
        self.setFaultConditions()

        ### Update loop
        while True:
            self.updateValues()
            # Convert to values
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

    def defineDatabaseConnection(self):
        pass

    def setFaultConditions(self):
        pass


if __name__ == "__main__":
    ###User input
    runner = Runner(True)
    runner.Run()
    print(runner)
