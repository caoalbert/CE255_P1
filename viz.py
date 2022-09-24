from matplotlib import pyplot as plt
import seaborn as sns

def viz_heatmap(df, name):
    df["time"] = df["5 Minutes"].dt.time
    df["time"] = df["time"].astype("str")
    plt.figure(figsize = (15,8))
    p1 = sns.heatmap(df.pivot("position", "time", "Speed (mph)"))
    p1.set(title = name)
    return p1

