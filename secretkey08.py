import secrets
import time

# start time
t1 = time.process_time()

print("")

import secrets

# Generate 24 API keys
for i in range(24):
    api_key = secrets.token_hex(8)
    print(api_key)


# end time
t2 = time.process_time()
time_diff = round(t2 - t1,8)

print("")
print("----------------------------------------------------------------")
print(f"It took {time_diff} Secs to generate these secret keys")
print("----------------------------------------------------------------")
print("")