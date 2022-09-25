def travel_time(df, po, time, begin = None, end = None):
    loop_detector_coverage = {}
    
    for i in range(len(po)):
        if i == 0:
            loop_detector_coverage[po[i]] = (po[i+1] - po[i])/2
            
        elif i == (len(po)-1):
            loop_detector_coverage[po[i]] = (po[i] - po[i-1])/2        
        else:
            dis = (po[i] - po [i-1])/2 + (po[i+1] - po [i])/2
            loop_detector_coverage[po[i]] = dis
            
    t = 0
    for i in po:
        x = loop_detector_coverage[i]
        v = df[(df["position"] == i) & (df["time"] == time)]["Speed (mph)"].item()
        
        if begin is not None:
            if (i <= begin) & (i >= end):
                v = 60
        t = t + x/v
    return t*60



