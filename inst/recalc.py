import datetime
import numpy as np
from read_pems import read_pems


    
df_913, t_913, po_913 = read_pems(datetime.date(2022, 9, 13))

output = np.empty(shape = (1,3))

bna_913 = po_913[0:14]
bna_913.reverse()

                            
for i in t_913[100:140]:
    print("The time is at", i, "\n")
    for j in range(len(bna_913)-2):
           xi = bna_913[j]
           for k in range(j+2, len(bna_913)):
               xj = bna_913[k]
               for m in range(j, k-1):
                   xk = bna_913[m]
                   for n in range(m+1, k):
                       xl = bna_913[n]
                       if xi - xj < 2:
                          vxk = df_913[(df_913["position"] == xk) & (df_913["5 Minutes"].dt.time  == i)]["Speed (mph)"].to_list()[0]
                          vxl = df_913[(df_913["position"] == xl) & (df_913["5 Minutes"].dt.time  == i)]["Speed (mph)"].to_list()[0]
                          if vxk - vxl > 0:
                              vxj = df_913[(df_913["position"] == xj) & (df_913["5 Minutes"].dt.time  == i)]["Speed (mph)"].to_list()[0]
                              vxi = df_913[(df_913["position"] == xi) & (df_913["5 Minutes"].dt.time  == i)]["Speed (mph)"].to_list()[0]
                              if vxj - vxi > 20:
                                  if vxi < 40:
                                      output = np.append(output, [[xi, xj, i]], axis = 0 )                           
            
            
output = output[1:]

from tempfile import TemporaryFile
outfile = TemporaryFile()
np.save(outfile, output)
_ = outfile.seek(0)
k = np.load(outfile)


bottle_neck = [output[0,]]
t0 = output[0,2]
int0 = output[0,0] - output[0,1]

for i in range(1, output.shape[0]):
    t = output[i,2]
    int = output[i,0] - output[i,1]
    if (t != t0) | (int > int0):
        bottle_neck = np.append(bottle_neck, [output[i,]], axis = 0)
        t0 = t
        int0 = int
        

bottle_neck = [output[0,]]  

       
    
        
t0 = output[0,2]
    int0 = output[0,0] - output[0,1]
    for i in range(1, output.shape[0]):
        t = output[i,2]
        int = output[i,0] - output[i,1]
        if (t != t0) | (int > int0):
            bottle_neck = np.append(bottle_neck, [output[i,]], axis = 0)
            t0 = t
            int0 = int
    
    
    
    
        
    
    


