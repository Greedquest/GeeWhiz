import random
import Semantic_Class as semantics


class SemanticMap(dict):
    def __init__(self, mapDict=None, dummyDataSize=5):

        if mapDict == None:
            # pre populate dict with random data if none provided
            super(SemanticMap, self).__init__(self._dummyMapping(dummyDataSize))

        else:
            super(SemanticMap, self).__init__(mapDict)

    def _dummyMapping(self, dataSize):

        return {outputID: _randomSemanticClass() for outputID in range(dataSize)}


def _randomSemanticClass():
    randID = random.randint(0, 100)
    possibleTypes = (
        semantics.Discrete(f"Button {randID}"),
        semantics.LCDDisplay(f"LCD {randID}"),
        semantics.ContinuousDial(f"ContinuousDial {randID}"),
    )

    return random.choice(possibleTypes)


if __name__ == "__main__":
    s = SemanticMap()
    for key in s.keys():
        print(key, type(s[key]), s[key].meaning)
