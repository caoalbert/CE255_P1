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
    
    t0 = output[0,2]
    int0 = output[0,0] - output[0,1]
    for i in range(1, output.shape[0]):
        t = output[i,2]
        int = output[i,0] - output[i,1]
        if (t != t0) | (int > int0):
            bottle_neck = np.append(bottle_neck, [output[i,]], axis = 0)
            t0 = t
            int0 = int
            
    return bottle_neck
    
