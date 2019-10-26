# -*- coding: utf-8 -*-

# USE THESE ON SEMANTIC CLASS MODULE IF U WANNA TEST
#Example_semanticmap   = {"ID1":Needle_test,"ID2":test,"ID3":Switchvalue}
#Example_conditionsmap = {"ID1":[5,25],"ID2":"On","ID3":"middle"}


def ConditionCheck(conditions_map, semantic_map):
    """
    TERMINOLOGY
    [Semantic Object: a dial of sorts; one of the three inherited classes of "Semantic"]
    [Semantic Map: a dictionary of this form, created at configuration {OutputID:Semantic Object}]
    
    Preferred input*: 
        {OutputID:Conditions} with as many SIMULTANEOUS conditions as needed
        {OutputID:Semantic Objects}
        
    For objects with continuous values (continuous dials), the condition should be [lower limit,upper limit]
        It will give True if the value is below a lower limit or above the upper
        Replace l limit with False if you don't want a lower limit
    For objects with string conditions "On", just give "On". Capitalisation inconsistencies don't matter
    
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
        