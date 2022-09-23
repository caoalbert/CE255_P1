import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

files = os.listdir("data/")

miles = []
for i in files:
    pos = i.split()[1].split(".csv")[0]
    miles.append(float(pos))
miles.sort()
miles


df = pd.DataFrame()
for i in files:
    path = "data/" + i
    a = path.split()[1]
    position = a[:a.index(".csv")]
    
    new = pd.read_csv(path)
    new["position"] = position
    new["position"] = new["position"].astype("float64")
    df = pd.concat([df, new], 0)
    
section_length = []
for i in np.arange(1, len(df)-1):
    section = df["position"][i]-df["position"][i-1]
    section_length.append(section)

df["section length"] = section_length






df2 = df[["position", "Speed (mph)", "5 Minutes"]]
df2["5 Minutes"] = pd.to_datetime(df2["5 Minutes"])


df2["time"] = df2["5 Minutes"].dt.time
df2["date"] = df2["5 Minutes"].dt.date
df2["time"] = df2["time"].astype("str")
df2["date"] = pd.to_datetime(df2["date"])



df3 = df2.loc[df2["date"] == "2022-09-13"][["position", "Speed (mph)", "time"]]
plt.figure(figsize = (15,8))
p1 = sns.heatmap(df3.pivot("position", "time", "Speed (mph)"))
p1.set(title = "9-13")
plt.savefig("9-13.png", dpi = 600)


df4 = df2.loc[df2["date"] == "2022-09-14"][["position", "Speed (mph)", "time"]]
plt.figure(figsize = (15,8))
p2 = sns.heatmap(df4.pivot("position", "time", "Speed (mph)"))
p2.set(title = "9-14")
plt.savefig("9-14.png", dpi = 600)


df5 = df2.loc[df2["date"] == "2022-09-15"][["position", "Speed (mph)", "time"]]
plt.figure(figsize = (15,8))
p3 = sns.heatmap(df5.pivot("position", "time", "Speed (mph)"))
p3.set(title = "9-15")
plt.savefig("9-15.png", dpi = 600)



df3_bn1 = df3.query('position >= 10 and position <= 12.83')
df3_bn1["time"] = pd.to_datetime(df3_bn1["time"])
df3_bn1 = df3_bn1.set_index("time").between_time("7:30", "9:30")
sns.distplot(df3_bn1["Speed (mph)"], hist = True)
plt.show()


def find_delay(df, dt, dx, tt):
    
    df["time"] = pd.to_datetime(df["time"])
    df_night = df.set_index("time").between_time("00:00", "06:00")
    free_flow_speed = df_night["Speed (mph)"].mean()
    
    df_cross = df[(df["position"] <= dx[0]) & (df["position"] >= dx[1])]
    bn_speed = df_cross.set_index("time").between_time(dt[0], dt[1])["Speed (mph)"].mean()
    
    l = dx[0]-dx[1]
    delay = l*(1/bn_speed-1/free_flow_speed)*60
    
    
    if tt == True:
        return l/bn_speed*60
    else:
        print(free_flow_speed)
        return delay


dt_bn1_913 = ["07:30", "07:30"]
dx_bn1_913 = [12.83, 10.8]

dt_bn2_913 = ["08:45", "09:10"]
dx_bn2_913 = [9.45, 6.92]

dt_bn1_914 = ["8:20", "8:20"]
dx_bn1_914 = [12.83, 10.8]

dt_bn2_914 = ["08:45", "08:45"]
dx_bn2_914 = [8.11, 6.92]

dt_bn1_915 = ["7:55", "9:10"]
dx_bn1_915 = [12.83, 10.8]

dt_bn2_915 = ["8:45", "8:45"]
dx_bn2_915 = [7.74, 6.92]

find_delay(df5, dt_bn1_915, dx_bn1_915, False)


find_delay(df4, dt_bn1_914, dx_bn1_914, True)

find_delay(df3, dt_bn1_913, dx_bn1_913, False)
find_delay(df3, dt_bn2_913, dx_bn2_913, False)
find_delay(df4, dt_bn1_914, dx_bn1_914, False)
find_delay(df4, dt_bn2_914, dx_bn2_914, False)
find_delay(df5, dt_bn1_915, dx_bn1_915, False)
find_delay(df5, dt_bn2_915, dx_bn2_915, False)

dt_nonrec = ["17:30", "17:55"]
dx_nonrec = [4.84, 3.73]
find_delay(df4, dt_nonrec, dx_nonrec, False)