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
        
        def find_nearest(array, value):
           
            stateArray = np.array(list(array))
            differenceArray = np.abs(stateArray - value)
            idx = differenceArray.argmin()
            return stateArray[idx]
        
        "A Discrete value lookup will map state to the closest matching value for comparable types, or exact match for anything else"
        try:
            self._value = self._valueMap[state]
        
        except KeyError:
            self._value = self._valueMap[find_nearest(self._valueMap.keys(), state)]
        
        
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
        
def ConditionCheck(conditions_map, semantic_map):
    """
    TERMINOLOGY
    [Semantic Object: a dial of sorts; one of the three inherited classes of "Semantic"]
    [Semantic Map: a dictionary of this form, created at configuration {OutputID:Semantic Object}]
    
    Preferred input*: 
        {OutputID:Conditions}
        {OutputID:Semantic Objects}
    The idea is that this would be produced alongside an {OutputID:Semantic Object} at the start
    """
    
    conditions = {} # An empty {Semantic Object:Conditions} object
    for i in conditions_map:
        # i becomes key, and we retain the same value as in semantic_map dictionary
        conditions[semantic_map[i]] = conditions_map[i] 
        
    Result = []
    count = 0
    for i in conditions:
        
        Result.append(0)
        
        # If i represents a continuous dial
        if type(conditions[i])==list:
            
            if conditions[i][0]==False & conditions[i][1]==True: # Only an upper limit
                Result[count] = (i.value>conditions[i][1]) 
                
            if conditions[i][1]==False & conditions[i][0]==True: # Only a lower limit
                Result[count] = (i.value<conditions[i][0]) 
                
            else:   # allowable RANGE
                Result[count] = (i.value<conditions[i][0])or(i.value>conditions[i][1]) 
                
        # If i represents a discrete dial where True is already mapped to a string e.g. "Off"
        if type(conditions[i])==str:
            Result[count]=(i.value.upper()==conditions[i].upper())
            
        count += 1
        
    if Result.count(True)==len(Result):
        return True
    else:
        return False
   
if __name__=="__main__":
    
    niceDiscrete = Discrete("Oven fan switch",{"On":"YASSS","Off":"NAY"})
    nastyDiscrete = Discrete("Bakery dial",{-30:"left",0:"middle",30:"right"})
    
    niceDiscrete.value = "On"
    assert niceDiscrete.value == "YASSS"
        
    nastyDiscrete.value = 0
    assert nastyDiscrete.value == "middle"
    
    
    nastyDiscrete.value = 15.5
    print(nastyDiscrete.value)
    
#    test = Discrete("Fan Oven Status")
#    test.value = True
#    print(test.meaning, test.value)
#    print(test._valueMap)
#    
#    Switchvalue = Discrete("Oven Power", {0:"left",1:"middle",2:"right"})
#    Switchvalue.value = 1
#    print(Switchvalue.meaning, Switchvalue.value)
#    
#    Needle_test = ContinuousDial("Voltage", 20,-20,40,0)
#    Needle_test.value = 10
#    print(Needle_test.meaning, Needle_test.value)
#    
#    Example_semanticmap   = {"ID1":Needle_test,"ID2":test,"ID3":Switchvalue}
#    Example_conditionsmap = {"ID1":[5,25],"ID2":"On","ID3":"middle"}
#    
#    #ConditionsMap = {Needle_test:[5,35],test:"On",Switchvalue:"middle"} # Test conditions 
#    
#    print(ConditionCheck(Example_conditionsmap,Example_semanticmap))
#    
    

            
    
            

    
    