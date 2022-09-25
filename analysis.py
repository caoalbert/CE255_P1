from read_pems import read_pems
from bottle_neck_detection import bottle_neck_detection
from delay_calc import delay_calc
from viz import viz_heatmap
from travel_time import travel_time
import datetime
import matplotlib.pyplot as plt
import numpy as np

# Recurrent bottleneck on 9/13
df_913, t_913, po_913 = read_pems(datetime.date(2022, 9, 13))
output_913, bottle_neck_913 = bottle_neck_detection(df_913, t_913, po_913, 10.4, 6.63)
delay_calc(df_913, po_913, bottle_neck_913[1:], 60)
viz_heatmap(df_913, "9-13")
plt.savefig("img/9-13.png", dpi = 600)

# Recurrent bottleneck on 9/14
df_914, t_914, po_914 = read_pems(datetime.date(2022, 9, 14))
output_914, bottle_neck_914 = bottle_neck_detection(df_914, t_914, po_914, 9.04, 6.63)
delay_calc(df_914, po_914, bottle_neck_914, 60)
viz_heatmap(df_914, "9-14")
plt.savefig("img/9-14.png", dpi = 600)

# Recurrent bottleneck on 9/15
df_915, t_915, po_915 = read_pems(datetime.date(2022, 9, 15))
output_915, bottle_neck_915 = bottle_neck_detection(df_915, t_915, po_915, 9.04, 6.63)
delay_calc(df_915, po_915, bottle_neck_915, 60)
viz_heatmap(df_915, "9-15")
plt.savefig("img/9-15.png", dpi = 600)


# Non-recurrent bottle neck
output_914_nr, bottle_neck_914_nr = bottle_neck_detection(df_914, t_914, po_914, 5.46, 0.47)

bottle_neck_914_nr = np.array([[0,0,0]])
for i in [17,18]:
    if i == 17:
        for j in [i*5 for i in range(4, 12)]:
            c = np.array([[4.84, 3.37, datetime.time(i,j)]])
            bottle_neck_914_nr = np.append(bottle_neck_914_nr, c, axis = 0)
            
    if i == 18:
        for j in [i*5 for i in range(0,3)]:
            c = np.array([[4.84, 3.37, datetime.time(i,j)]])
            bottle_neck_914_nr = np.append(bottle_neck_914_nr, c, axis = 0)
bottle_neck_914_nr = bottle_neck_914_nr[1:,]  
    
a = delay_calc(df_914, po_914, bottle_neck_914_nr, 60)

b = delay_calc(df_913, po_913, bottle_neck_914_nr, 60)
c = delay_calc(df_915, po_915, bottle_neck_914_nr, 60)
d = (b+c)/2
d+(a-d)/3

# Travel Times
# Recurrent
time = datetime.time(9,10)
tt_913_ff = travel_time(df_913, po_913, time, 8.11, 6.63)
tt_913 = travel_time(df_913, po_913, time)

time = datetime.time(8,40)
tt_914_ff = travel_time(df_914, po_914, time, 7.74, 6.63)
tt_914 = travel_time(df_914, po_914, time)

tt_915_ff = travel_time(df_915, po_915, time, 7.74, 6.63)
tt_915 = travel_time(df_915, po_915, time)

tt_913 - tt_913_ff
tt_914 - tt_914_ff
tt_915 - tt_915_ff

# Non-recurrent
time = datetime.time(17,30)
tt_914_ff_nr = travel_time(df_914, po_914, time, 4.84, 3.37)
tt_914_nr = travel_time(df_914, po_914, time)
