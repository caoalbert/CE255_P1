import pandas as pd

def delay_calc(df, po, bn, vf):
    loop_detector_coverage = {}
    for i in range(len(po)):
        if i == 0:
            loop_detector_coverage[po[i]] = (po[i+1] - po[i])/2
        
        elif i == (len(po)-1):
            loop_detector_coverage[po[i]] = (po[i] - po[i-1])/2
        
        else:
            dis = (po[i] - po [i-1])/2 + (po[i+1] - po [i])/2
            loop_detector_coverage[po[i]] = dis
    
    df["time"] = pd.to_datetime(df["5 Minutes"])
    df["time"] = df["time"].dt.time

    delay = []
    for j in range(bn.shape[0]):
        
        begin = po.index(bn[j,][1])
        end = po.index(bn[j,][0])
        time = bn[j,][2]
        
        for i in range(begin, end+1):
            flow = df[(df["position"] == po[i]) & (df["time"] == time)]["Flow (Veh/5 Minutes)"].item()
            speed = df[(df["position"] == po[i]) & (df["time"] == time)]["Speed (mph)"].item()
            di = loop_detector_coverage[po[i]]
            vmt_i = flow*di
            vht_i = vmt_i / speed
            delay_i = max(vht_i-vmt_i/vf, 0)
            delay.append(delay_i)
            
    return delay
        


