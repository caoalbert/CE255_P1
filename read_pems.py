import os
import pandas as pd

def read_pems(day):
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
    
