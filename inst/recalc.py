import datetime
import os
import pandas as pd
import numpy as np

def read(day):
    files = os.listdir("data/")
    output = pd.DataFrame()
    
    for i in files:
        path = "data/" + i
        a = path.split()[1]
        position = a[:a.index(".csv")]

        new = pd.read_csv(path)
        new["5 Minutes"] = pd.to_datetime(new["5 Minutes"])
        new["day"] = new["5 Minutes"].dt.date
        new = new[new["day"] == day]
        
        new["position"] = position
        new["position"] = new["position"].astype("float64")
        output = pd.concat([output, new], 0)
        
    output.sort_values(["5 Minutes", "position"], inplace = True)
    time_interval = output["5 Minutes"].dt.time.unique().tolist()
    positions = output["position"].unique().tolist()
    
    return (output, time_interval, positions)
    
df_913, t_913, po_913 = read(datetime.date(2022, 9, 13))

output = np.empty(shape = (1,3))

bna_913 = po_913[-8:]
bna_913.reverse()




for i in t_913[0:1]:
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
        
        


        

        
    
    


