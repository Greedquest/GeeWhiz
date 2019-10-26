from abc import ABC, abstractmethod
import numpy as np

# Create grandaddy class to cover all semantic classes
class Semantic(ABC):
    def __init__(self,meaning):
        self.meaning = meaning
        self._value = None
        
    def __repr__(self):
        return self.meaning
        
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
    
    ValueMap should have the following possible inputs, depending on what is commented: 
        
    [all angles measured off the vertical, with clockwise positive]
    OPTION A: You know the current angle from vision, read the current value and zero value
    OPTION B: You know/measure the extreme values and angles (min_angle expected negative)
    
    Note therefore initial calibration will be needed
    """
    
    # OPTION A
#    def __init__(self, meaning, start_angle, start_value, zero_value):
#        self._start_angle = start_angle
#        self._start_value = start_value
#        self._zero_value  = zero_value
    # OPTION B
    def __init__(self, meaning, min_angle, max_angle, min_val, max_val):
        self._max_angle = max_angle
        self._min_angle = min_angle
        self._max_val   = max_val
        self._min_val   = min_val
        
        super(ContinuousDial,self).__init__(meaning)
    
    # OPTION A
#    @Semantic.value.setter
#    def value(self,angle):
#        angle_proportion = abs(self._start_value-self._zero_value)/abs(self._start_angle)
#        state = self._zero_value + (angle_proportion * angle)
#        self._value = state
        
    # OPTION B
    @Semantic.value.setter
    def value(self,angle):
        state = ((angle - self._max_angle)*(self._min_angle-self._max_angle)) / (self._min_val-self._max_val)
        self._value = state
        
        
        
        
class LCDDisplay(Semantic):
    "Parent class that covers word or number LCD displays"
    
    @Semantic.value.setter
    def value(self,state):
        self._value = state
 

### TESTS        
   
if __name__=="__main__":
    
    test = Discrete("Fan Oven Status")
    test.value = True
    print(test.meaning, test.value)
    print(test._valueMap)
    
    Switchvalue = Discrete("Oven Power", {0:"left",1:"middle",2:"right"})
    Switchvalue.value = 1
    print(Switchvalue.meaning, Switchvalue.value)
    
    Needle_test = ContinuousDial("Voltage", 20,-20,40,0)
    Needle_test.value = 10
    print(Needle_test.meaning, Needle_test.value)
    
    
    Conditions = {Needle_test:[5,35],test:"On"} # Test conditions 
    Result = {}
    
    for i in Conditions:
        if type(Conditions[i])==list:
            Result[i]=(i.value<Conditions[i][0])or(i.value>Conditions[i][1])
        if type(Conditions[i])==str:
            Result[i]=(i.value.upper()==Conditions[i].upper())
            
            

    
    