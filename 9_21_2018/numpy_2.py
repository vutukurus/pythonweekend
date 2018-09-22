import numpy as np
csv = np.genfromtxt ('pandas_csv.csv', delimiter=",") 

print csv[1:6,2] 
print csv
