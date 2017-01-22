#For reading data from files in one director and modifying it accordingly to the task (in this case: kinetics)
import numpy as np
import glob
from io import StringIO
import os

path = "/PathToFile/*.csv"
files = glob.glob(path)

print("Files written:")
for file in files:
    filename = os.path.basename(file)
    f  = open(filename ,'w')
    #read array from datafile
    g = np.genfromtxt(file, delimiter = "        ",)
    #calulate the average of the beginning to get a 0 value which is substracted
    #from the y values.
    ovalue = np.genfromtxt(file, delimiter = "        ", max_rows = 75)
    fneveruse, yovalue = np.hsplit(ovalue, 2)
    fy0 = np.mean(yovalue)
    ffy0 = float(fy0)
    
    fx, fy = np.hsplit(g, 2)
#Modify the data the way you need it
    A = (ffy0/fy)
    DeltaA = np.log(A)
    DeltaA1k = np.log(DeltaA)
    
    dataarray = np.concatenate((fx, DeltaA1k), axis = 1)
    
    #to have some output
    print (filename)
    
    np.savetxt(filename, dataarray, delimiter = '        ', fmt = '%8f')
    f.close()    
print("Done :)")
