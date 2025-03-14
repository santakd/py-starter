import uuid
import time
import memory_profiler  # type: ignore

def generate_uuids(n=24):
    """Generate and print `n` UUIDs in Microsoft format."""
    for _ in range(n):
        ms_uuid = '{' + str(uuid.uuid4()).upper() + '}'
        print(ms_uuid)

def measure_performance():
    """Measure and print the time and memory usage of the UUID generation."""
    # Start memory usage
    start_memory = memory_profiler.memory_usage()

    # Start time
    start_time = time.process_time()

    print("")

    # Generate UUIDs
    generate_uuids()

    # End time
    end_time = time.process_time()

    # End memory usage
    end_memory = memory_profiler.memory_usage()

    # Calculate differences
    memory_diff = round(end_memory[0] - start_memory[0], 8)
    time_diff = round(end_time - start_time, 8)

    print("")
    print("----------------------------------------------------------------")
    print(f"It took {time_diff} seconds and {memory_diff} MB to execute this program")
    print("----------------------------------------------------------------")
    print("")

def main():
    """Main function to run the script."""
    measure_performance()

if __name__ == "__main__":
    main()