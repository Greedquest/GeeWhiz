from abc import ABC, abstractmethod
import numpy as np

# Create grandaddy class to cover all semantic classes
class Semantic(ABC):
    def __init__(self,meaning):
        self.meaning = meaning
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
    
    def __init__(self,meaning,valueMap={True:"On",False:"Off"}):
        self._valueMap = valueMap
        super(Discrete,self).__init__(meaning)
    
    @Semantic.value.setter
    def value(self,state):
        self._value = self._valueMap[state]
        
        
class ContinuousDial(Semantic):
    """
    Dial that can rotate through an angle less than 360 degrees
    
    ValueMap should have the following input: (mintheta,maxtheta,minval,maxval,val_at_0)
    """
    
    def __init__(self,meaning,valueMap):
        self._valueMap = valueMap
        super(Discrete,self).__init__(meaning)
    
#    @Semantic.value.setter
#    def value(self,angle):
#        angle_proportion = ()/()
#        state = angle_proportion * (valueMap[4])
#        self._value = state
        
class NeedleDial(Semantic):
    """
    Dial that can rotate through an angle less than 360 degrees
    
    ValueMap should have the following input: (start_theta, start_val,val_at_0)
    Note therefore initial calibration will be needed
    """
    
    def __init__(self,meaning,valueMap):
        self._valueMap = valueMap
        super(NeedleDial,self).__init__(meaning)
        
    @Semantic.value.setter
    def value(self,angle):
        angle_proportion = abs(self._valueMap[1]-self._valueMap[2])/abs(self._valueMap[0])
        state = self._valueMap[2] + (angle_proportion * angle)
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
    print(test.meaning, test.value)
    
    Switchvalue = NDial("Oven Power", {0:"left",1:"middle",2:"right"})
    Switchvalue.value = 1
    print(Switchvalue.meaning, Switchvalue.value)
    
    Needle_test = NeedleDial("Voltage", (-10,5,7))
    Needle_test.value = 10
    print(Needle_test.meaning, Needle_test.value)
    
    