import datetime
from read_pems import read_pems
from bottle_neck_detection import bottle_neck_detection
import numpy as np




df_913, t_913, po_913 = read_pems(datetime.date(2022, 9, 13))


output, bottle_neck = bottle_neck_detection(df_913, t_913, po_913, 10.4, 6.63)
