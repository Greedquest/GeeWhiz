from abc import ABC, abstractmethod

# Create grandaddy class to cover all semantic classes
class Semantic(ABC):
    def __init__(self,name):
        self.name = name
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
    
    def __init__(self,name,valueMap={True:"On",False:"Off"}):
        self._valueMap = valueMap
        super(Discrete,self).__init__(name)
    
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
        
class Switch(Discrete):
    "The up/down switches"
    
    @Semantic.value.setter
    def value(self,state):
        self._value = state
    
class Button(Discrete):
    "The big buttons that can be red/green"
    
    
class LED(Discrete):
    "On/Off light switches"
    
        
class LCDNumerical(LCDDisplay):
    "The LCD screens that display numerical data"

        
class LCDText(LCDDisplay):
    "The LCD screens that display rolling text"
    

        
        
   
if __name__=="__main__":
    
    test = Discrete("Barry")
    test.value = True
    print(test.name, test.value)
    
    Switchvalue = Discrete("3 way switch", {0:"left",1:"middle",2:"right"})
    Switchvalue.value = 1
    print(Switchvalue.name, Switchvalue.value)
    
    