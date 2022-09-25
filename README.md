# CE255 Project 1

`read_pems.py` contains a function called `read_pems()` that cleans the raw PEMS data.

Inputs:

1. day: A datetime object

Outputs:

A tuple of length 3:

1. A merged and cleaned dataframe containing PEMS data of the day specified
2. A list of timestamps in the dataframe
3. A list of loop detector positions.

---

`bottle_neck_detection.py` contains a function called `bottle_neck_detection()` that returns the intervals at which bottlenecks exist

Inputs:

1. df: A dataframe processed by `read_pems()` 
2. t: A list of timestamps, output by `read_pems()`
3. po: A list of positions, output by `read_pems()`
4. begin: An float, the upstream position
5. end: An float, the downstream position

*Note: The upstream and downstream positions must at the location of the loop detectors

Outputs:

A tuple of length 2

1. A numpy array of dimension n x 3 that contains all bottleneck intervals at timestamps
2. A numpy array of dimension n x 3 that contains a single bottleneck interval at each unique timestamp

---

`delay_calc.py` contains a function called `delay_calc()` that takes 4 arguments to calculate the total delay in vehicle hours in the given section.

Inputs:

1. df: A dataframe processed by `read_pems()`
2. po: A list of positions, output by `read_pems()`
3. bn: A numpy array of unique bottlenecks at each timestamp, processed by `bottle_neck_detection.py`
4. vf: A float/int of reference flow speed

Output:

1. A float of total delay in the specified section

--- 

`travel_time` contains a function called `travel_time()` that calculates the travel time in the entire stretch of the section. 

Inputs:

1. df: A dataframe processed by `read_pems()`
2. po: A list of positions, output by `read_pems()`
3. time: A datetime object that specifies the timestamp at which the travel time calculation is conducted
4. begin: An optional input that is supplied when calculating travel time if had not been delayed by the section specified starting at begin and terminates at end
5. end: An optional argument specifing the end of the segment

*Note: If argument 4 and 5 are missing, then the function computes the actual travel time

Ouptut:

1. A float of travel time in minutes

---

`viz.py` contains a function called `viz_heatmap` that creates a heatmap of the bottleneck.

Inputs:

1. A dataframe processed by `read_pems()`
2. A string for the name of the heatmap

Output:

1. A plot object 


