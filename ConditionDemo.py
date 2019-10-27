# -*- coding: utf-8 -*-
from E3.Fault_Conditions import ConditionCheck
import DataCollation.Semantic_Class as sem
from Email import dispatchFaultMessage
from UserInput import ConditionMapCreator
import pandas as pd

example_button = sem.Discrete("BOILER ON")
example_button.value=True
example_three_state = sem.Discrete("BOILER MODE",{-45:"LEFT",0:"MIDDLE",45:"RIGHT"})
example_three_state.value= 20
example_needle = sem.ContinuousDial("HEAT GAUGE",-30,30,0,20)
example_needle.value=-29
example_semantic_map = {1:example_button,2:example_three_state,3:example_needle}

file = pd.read_csv(r"C:\Users\Tomos\Documents\Programming, Projects\Python\IfM Hackathon\conditions.csv")

ConditionMaps = ConditionMapCreator(example_semantic_map,file)

testmap = ConditionMaps[1]
ConditionCheck(testmap,example_semantic_map)

if ConditionCheck(testmap,example_semantic_map)==True:
    dispatchFaultMessage(testmap,example_semantic_map,"tww26@cam.ac.uk")
