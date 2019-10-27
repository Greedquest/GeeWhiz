# -*- coding: utf-8 -*-
import pandas as pd

#file = pd.read_csv(r"C:\Users\Tomos\Documents\Programming, Projects\Python\IfM Hackathon\conditions.csv")

def ConditionMapCreator(semantic_map,file):
    "Produces a list of condition maps from a given file"
     
    ConditionMapList = []
    # i for every row that exists
    for i in range(len(file[file.columns[0]].values)):
        # Create a condition map
        ConditionMap = {}
        # Looks at how many conditions are within condition map
        for j in range(file[file.columns[1]].values[i]):
            # Add key:reference = semantic_object = condition
            
            # What is the ID of the semantic object which has a condition?
            ObjectID = file[file.columns[2+j]].values[i]
            # What is the condition? DEPENDS ON THE TYPE
            
            if type(semantic_map[ObjectID])==ContinuousDial:
                Condition = []
                Condition.append(float(file[file.columns[4+2*j]].values[i]))
                Condition.append(float(file[file.columns[5+2*j]].values[i]))
            else: # DISCRETE
                Condition = str(file[file.columns[4+j*2]].values[i])
                
            # Add this as a key
            ConditionMap[ObjectID] = Condition
            
        ConditionMapList.append(ConditionMap)
        
    return ConditionMapList
            
        
    
