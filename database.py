'''
Database module 
Write semantic objects to a csv file to log outputs

'''

import csv
import datetime
from SemanticOutputMap import SemanticMap


"""function to make header rows as a new csv file
input a list of the semantic object"""

def define_log(SOs):

    try:
        
        with open('log.csv','w') as f:
            w = csv.writer(f, delimiter = ',')
            w.writerow(['Time'] + [semanticObj.meaning for semanticObj in SOs])

    except IOError:

        with open('log.csv','w+') as f:
            w = csv.writer(f, delimiter = ',')
            w.writerow(['Time'] + [semanticObj.meaning for semanticObj in SOs])
        

"""
function to append new data to log.csv file
input a list of the semantic object
"""
def write_to_log(SOs):

    with open('log.csv','a') as f:
        w = csv.writer(f, delimiter = ',')
        w.writerow([datetime.datetime.now()] + [semanticObj.values for semanticObj in SOs])
     
     
if __name__ == '__main__':
    
    # test module
    semantic_objects = SemanticMap()  #a list of semantic objects
    for i in semantic_objects:
        semantic_objects[i].values = 12
    #print(semantic_objects)
    
    define_log(semantic_objects.values())
    
    for i in range(10):
        write_to_log(semantic_objects.values())