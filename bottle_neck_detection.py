import numpy as np


def bottle_neck_detection(df, t, po, begin, end):
    
    output = np.empty(shape = (1,3))
    sec = po[po.index(end):po.index(begin)]
    sec.reverse()
    
    
    for i in t:
        print("The time is at", i, "\n")
        for j in range(len(sec)-2):
            xi = sec[j]
            for k in range(j+2, len(sec)):
                xj = sec[k]
                for m in range(j, k-1):
                    xk = sec[m]
                    for n in range(m+1, k):
                        xl = sec[n]
            
                        if xi - xj < 2:
                            vxk = df[(df["position"] == xk) & (df["5 Minutes"].dt.time  == i)]["Speed (mph)"].to_list()[0]
                            vxl = df[(df["position"] == xl) & (df["5 Minutes"].dt.time  == i)]["Speed (mph)"].to_list()[0]
                            if vxk - vxl > 0:
                                vxj = df[(df["position"] == xj) & (df["5 Minutes"].dt.time  == i)]["Speed (mph)"].to_list()[0]
                                vxi = df[(df["position"] == xi) & (df["5 Minutes"].dt.time  == i)]["Speed (mph)"].to_list()[0]
                                if vxj - vxi > 20:
                                    if vxi < 40:
                                        output = np.append(output, [[xi, xj, i]], axis = 0 )
    
    output = output[1:]
    bottle_neck = [output[0,]]
    
    max0 = output[0,0]
    min0 = output[0,1]
    t0 = output[0,2]
    a = 1
    while a < output.shape[0]-1:
        if a > 1:
            bottle_neck = np.append(bottle_neck, [[max0, min0, output[a,2]]], axis  = 0)
            max0 = output[a,0]
            min0 = output[a,1]
            t0 = output[a,2]
            a += 1
        
        while t0 == output[a,2]:
            if output[a,0] > max0:
                max0 = output[a,0]
            if output[a,1] < min0:
                min0 = output[a,1]    
            a += 1
            if a >= output.shape[0]:
                break
        if a >= output.shape[0]:
            break
    
 
            


    return output
    
