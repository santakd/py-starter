import numpy as np
import random as rd
import time as tm

# start time
t1 = tm.process_time()

r = rd.randint(0, 255)
g = rd.randint(0, 255)
b = rd.randint(0, 255)

rgb_rd = [r, g, b]
print('A random rd color is:', rgb_rd)

rgb_np = list(np.random.choice(range(255), size=3))
print('A random np color is:', rgb_np)

# end time
t2 = tm.process_time()
time_diff = round(t2 - t1,8)

print("")
print("----------------------------------------------------------------")
print(f"It took {time_diff} Secs to generate these colors")
print("----------------------------------------------------------------")
print("")