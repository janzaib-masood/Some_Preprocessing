import numpy as np
import pandas as pd
import math
import os, sys
import ipdb as ipdb


def gimme(fileIndex):
    k = []; 
    for fileIndex in range(0+11*fileIndex,11*(fileIndex+1)):
        k.append(fileIndex)
    return k
def select_columns(dataframe, cols):
    return dataframe.loc[:, cols]

# detect the current working directory
#path = os.getcwd()

path = ''

fileNames = []
# read the entries
with os.scandir(path) as listOfEntries:  
    for entry in listOfEntries:
        # print all entries that are files
        if entry.is_file() and entry.name[-4:] == '.csv':
            fileNames.append(entry.name)
            print("Reading: ", entry.name) 
            
print('\n\nJust Read The FileNames\n\n\n')

# Results Folder to be created
folder = 'The_Results'
if os.path.exists("The_Results") == False:
    os.mkdir(folder);
path = path + '/' + folder

#ipdb.set_trace()

for fileN in fileNames:
    df = pd.read_csv(fileN)
    
    print("Total Size of Data = ", df.size)
    print("The Shape of Data  = ", df.shape)

    DateandTime = select_columns(df, ['Date','Time'])
    #ipdb.set_trace()
    df = df.drop(['Time', 'Date'], axis=1)

    num_of_files = int(math.floor(df.shape[1]-1)/11)
    num_of_files
    


    col_names = ['Date', 'Time', 'INSTANCE', 'TEMP_IN', 'TEMP_OUT', 'TEMP_HTX', 'TEMP_EXH','VOLU_CTL', 'FLOW_GPM',
                 'BYP_RATIO', 'FANSPEED','FLM_ROD','ALARM']
    for fileIndex in range(num_of_files):

        print("File Index = ", fileIndex)

        cols = gimme(fileIndex)

        thisFrame = df.iloc[:, cols]

        resultFrame = pd.concat([DateandTime, thisFrame],axis=1, sort=False)

        #resultFrame.to_csv(r'Path' + str(fileIndex)+ '.csv')
        resultFrame.columns = col_names

        resultFrame.to_csv(path+'/'+fileN[:-4] +'_' + str(fileIndex)+ '.csv')
        
        #ipdb.set_trace()

        
print("n\n\n\n\nAll Done!!!!!1")
