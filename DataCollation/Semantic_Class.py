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
        
class Binary(Semantic):
    "Binary components on the panel, including switches and lights"
    
    def __init__(self,name,valueMap={True:"On",False:"Off"}):
        self._valueMap = valueMap
        super(Binary,self).__init__(name)
    
    @Semantic.value.setter
    def value(self,state):
        self._value = self._valueMap[state]
        
class NDial(Semantic):
    "Dial that has N values on the dial"
    
    # Example value map is {[N,position]:value}
    def __init__(self,name,valueMap):
        self._valueMap = valueMap
        super(Ndial,self).__init__(name)
    
    @Semantic.value.setter
    def value(self,state):
        self._value = state
        
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
        
class Switch(Binary):
    "The up/down switches"
    
    @Semantic.value.setter
    def value(self,state):
        self._value = state
    
class Button(Binary):
    "The big buttons that can be red/green"
    
    
class LED(Binary):
    "On/Off light switches"
    
        
class LCDNumerical(LCDDisplay):
    "The LCD screens that display numerical data"

        
class LCDText(LCDDisplay):
    "The LCD screens that display rolling text"
    

        
        
   
if __name__=="__main__":
    
    test = Binary("Barry", {True:"On",False:"Off"})
    test.value = True
    print(test.name, test.value)
    
    Switchvalue = NDial("3 way switch", {0:"left",1:"middle",2:"right"})
    test.value = 1
    print(Switchvalue.name, Switchvalue.value)
    
    