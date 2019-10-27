from abc import ABC, abstractmethod
import numpy as np
import pandas as pd

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
    
    def __init__(self, meaning, min_angle, max_angle, min_val, max_val):
        self._stateRange = [min_angle,max_angle]
        self._valueRange = [min_val,max_val]
        
        super(ContinuousDial,self).__init__(meaning)
    
    
    @Semantic.value.setter
    def value(self,state):
        self._value = np.interp(state,self._stateRange, self._valueRange)
        
        
class LCDDisplay(Semantic):
    "Parent class that covers word or number LCD displays"
    
    @Semantic.value.setter
    def value(self,state):
        self._value = state
 

### TESTS  
        
#def ConditionCheck(conditions_map, semantic_map):
#    """
#    TERMINOLOGY
#    [Semantic Object: a dial of sorts; one of the three inherited classes of "Semantic"]
#    [Semantic Map: a dictionary of this form, created at configuration {OutputID:Semantic Object}]
#    
#    Preferred input*: 
#        {OutputID:Conditions}
#        {OutputID:Semantic Objects}
#    The idea is that this would be produced alongside an {OutputID:Semantic Object} at the start
#    """
#    
#    conditions = {} # An empty {Semantic Object:Conditions} object
#    for i in conditions_map:
#        # i becomes key, and we retain the same value as in semantic_map dictionary
#        conditions[semantic_map[i]] = conditions_map[i] 
#        
#    Result = []
#    count = 0
#    for i in conditions:
#        
#        Result.append(0)
#        
#        # If i represents a continuous dial
#        if type(conditions[i])==list:
#            
#            if conditions[i][0]==False and type(conditions[i][1])!=bool: # Only an upper limit
#                Result[count] = (i.value>conditions[i][1]) 
#                
#            if conditions[i][1]==False and type(conditions[i][0])!=bool: # Only a lower limit
#                Result[count] = (i.value<conditions[i][0]) 
#                
#            else:   # allowable RANGE
#                Result[count] = (i.value<conditions[i][0])or(i.value>conditions[i][1]) 
#                
#        # If i represents a discrete dial where True is already mapped to a string e.g. "Off"
#        if type(conditions[i])==str:
#            Result[count]=(i.value.upper()==conditions[i].upper())
#            
#        count += 1
#        
#    if Result.count(True)==len(Result):
#        return True
#    else:
#        return False
#    
#    
#def ConditionMapCreator(semantic_map,file):
#    "Produces a list of condition maps from a given file"
#     
#    ConditionMapList = []
#    # i for every row that exists
#    for i in range(len(file[file.columns[0]].values)):
#        # Create a condition map
#        ConditionMap = {}
#        # Looks at how many conditions are within condition map
#        for j in range(file[file.columns[1]].values[i]):
#            # Add key:reference = semantic_object = condition
#            
#            # What is the ID of the semantic object which has a condition?
#            ObjectID = file[file.columns[2+j]].values[i]
#            # What is the condition? DEPENDS ON THE TYPE
#            
#            if type(semantic_map[ObjectID])==ContinuousDial:
#                Condition = []
#                Condition.append(float(file[file.columns[4+2*j]].values[i]))
#                Condition.append(float(file[file.columns[5+2*j]].values[i]))
#            else: # DISCRETE
#                Condition = str(file[file.columns[4+j*2]].values[i])
#                
#            # Add this as a key
#            ConditionMap[ObjectID] = Condition
#            
#        ConditionMapList.append(ConditionMap)
#        
#    return ConditionMapList
#
### TESTS 
#if __name__=="__main__":
#    
#    example_button = Discrete("BOILER ON")
#    example_button.value=True
#    example_three_state = Discrete("BOILER MODE",{-45:"LEFT",0:"MIDDLE",45:"RIGHT"})
#    example_three_state.value= 20
#    example_needle = ContinuousDial("HEAT GAUGE",-30,30,0,20)
#    example_needle.value=-29
#    
#    
#    example_semantic_map = {1:example_button,2:example_three_state,3:example_needle}
#
#    file = pd.read_csv(r"C:\Users\Tomos\Documents\Programming, Projects\Python\IfM Hackathon\conditions.csv")
#    
#    MAP = ConditionMapCreator(example_semantic_map,file)
#    print(MAP[1])
#    print(ConditionCheck(MAP[0],example_semantic_map))
#    print(example_three_state.value)
#    print(ConditionCheck(MAP[1],example_semantic_map))


            
    
    

            
    
            

    
    