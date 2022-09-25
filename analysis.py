from read_pems import read_pems
from bottle_neck_detection import bottle_neck_detection
from delay_calc import delay_calc
from viz import viz_heatmap
import datetime
import matplotlib.pyplot as plt

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
delay_calc(df_914, po_914, bottle_neck_914_nr, 60)



