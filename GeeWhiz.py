from DataCollation.SemanticOutputMap import SemanticMap


class Runner:
    def __init__(self, dummyRun=True):
        self._useDummyData = dummyRun

    def Run(self):
        ###Get user input
        self.generateOutputMapping(self._useDummyData)
        self.defineNetworkConnection()
        self.setFaultConditions()

        ### Update loop
        while True:
            # Update readings
            # Convert to values
            # Add to database
            # check against error thresholds
            # if error then display alert
            break

        print("Done!")

    def generateOutputMapping(self, useDummyData=True):
        "Generate the mapping between Semantic objects and their ids"
        self.semanticMap = (
            SemanticMap()
        )  # SemanticMap(None if useDummyData else getMappingData)

    def defineNetworkConnection():
        pass

    def setFaultConditions():
        pass


if __name__ == "__main__":
    ###User input
    runner = Runner(True)
    runner.Run()
