import uuid
import time
import memory_profiler

# start memory usage
m1 = memory_profiler.memory_usage()

# start time
t1 = time.process_time()


print("")

# Generate 24 UUIDs
for i in range(24):
    print(uuid.uuid4())


# end time
t2 = time.process_time()

# end memory usage
m2 = memory_profiler.memory_usage()
    
mem_diff = round(m2[0] - m1[0],8)

time_diff = round(t2 - t1,8)

print("")
print("----------------------------------------------------------------")
print(f"It took {time_diff} Secs and {mem_diff} Mb to execute this program")
print("----------------------------------------------------------------")
print("")