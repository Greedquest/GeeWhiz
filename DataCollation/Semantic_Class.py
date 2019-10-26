from abc import ABC, abstractmethod

# Create grandaddy class to cover all semantic classes
class Semantic(ABC):
    def __init__(self,semantic_meaning):
        self.semantic_meaning = semantic_meaning
        self._value = None
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    @abstractmethod # Inherited classes must overwrite this or else run-time error
    def value(self, state):
        pass 
    
### INHERITED CLASSES ###
        
class Discrete(Semantic):
    "Binary components on the panel, including switches and lights"
    
    def __init__(self,semantic_meaning,valueMap={True:"On",False:"Off"}):
        self._valueMap = valueMap
        super(Discrete,self).__init__(semantic_meaning)
    
    @Semantic.value.setter
    def value(self,state):
        self._value = self._valueMap[state]
        
        
class ContinuousDial(Semantic):
    "Dial that can rotate the full 360 degrees"
    
    @Semantic.value.setter
    def value(self,state):
        self._value = state
        
class NeedleDial(Semantic):
    "Needle dials that have a range of "
    
    @Semantic.value.setter
    def value(self,state):
        self._value = state
        
class LCDDisplay(Semantic):
    "Parent class that covers word or number LCD displays"
    
    @Semantic.value.setter
    def value(self,state):
        self._value = state
        
### NEXT GENERATION INHERITED CLASSES
        
class Binary(Discrete):
    "The up/down switches, and the big buttons"
    
class NDial(Discrete):
    "Dial with discrete fixed points. Dictionary must account for this"
    
class LCDNumerical(LCDDisplay):
    "The LCD screens that display numerical data"
       
class LCDText(LCDDisplay):
    "The LCD screens that display rolling text"
    

        
        
   
if __name__=="__main__":
    
    test = Binary("Fan Oven Status")
    test.value = True
    print(test.semantic_meaning, test.value)
    
    Switchvalue = NDial("Oven Power", {0:"left",1:"middle",2:"right"})
    Switchvalue.value = 1
    print(Switchvalue.semantic_meaning, Switchvalue.value)
    
    