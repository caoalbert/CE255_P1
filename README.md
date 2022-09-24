# CE255 Project 1

`read_pems.py` contains a function called `read_pems()` that takes a `datetime` object and returns the a tuple of length 3 containing the joined dataframe with loop detection position, a list of timestamps in the dataframe, and a list of loop detection positions. 

`bottle_neck_detection.py` contains a function called `bottle_neck_detection()` that takes 5 arguments to detect bottle neck starting position and ending position during the 24 hr time window.

Inputs:

1. A dataframe processed by `read_pems()` 
2. A list of timestamps, output by `read_pems()`
3. A list of positions, output by `read_pems()`
4. An integer, the upstream position
5. An integer, the downstream position

*Note: The upstream and downstream positions must be the location of the loop detectors

Output:

A tuple of length 3 containing a numpy array of dimension nx3 that contains the qualifying position intervals and timestamps, and a cleaned numpy array of dimension nx3 where each 1x3 array contains `[starting position of bn, ending position of bn, timestamp]` where the position interval is the greatest at each time interval.



