from abc import ABC, abstractmethod

# Create grandaddy class to cover all semantic classes
class Semantic(ABC):
    def __init__(self,name):
        self.name = name
        self._value = None
        
    @property
    def value(self):
        return self._value
    
    @abstractmethod # Inherited classes must overwrite this or else run-time error
    @value.setter
    def value(self,state):
        pass  

# Inherited classes
class Binary(Semantic):
    "Binary components on the panel, including switches and lights"
    def __init__(self,):
        self._value 
        
class NState(Semantic):
    "Dial that has N values on the dial"
        
class ContinuousDial(Semantic):
    "Dial that can rotate the full 360 degrees"
        
class NeedleDial(Semantic):
    "Needle dials that have a range of "
        
class LCDDisplay(Semantic):
    "Parent class that covers word or number LCD displays"
   
        