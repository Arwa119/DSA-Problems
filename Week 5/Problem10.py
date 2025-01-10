from time import time

integers = []
append_times = []

for i in range(1, 101):
    start_time = time()
    integers.append(i)
    end_time = time()
    append_time = end_time - start_time
    append_times.append(append_time)

for i in range(100):
    print(f"Time taken to append {i+1}: {append_times[i]:.3f} seconds")


# The time taken to append integers will generally remain constant, as Python lists are highly optimized. 