import platform     # type: ignore
import psutil       # type: ignore
import subprocess   # type: ignore
import os.path      # type: ignore
import time         # type: ignore

# This function retrieves CPU information
def get_cpu_info():
    # Get processor info
    cpu_info = platform.processor()
    
    # Get number of CPUs
    num_cpus = psutil.cpu_count(logical=True)
    
    return f"CPU: {cpu_info}, Cores: {num_cpus}"

# This function retrieves memory information
def get_memory_info():
    # Get virtual memory details
    mem = psutil.virtual_memory()
    
    # Convert bytes to gigabytes for easy reading
    total_mem = round(mem.total / (1024 * 1024 * 1024), 2)
    used_mem = round(mem.used / (1024 * 1024 * 1024), 2)
    
    return f"Memory: {total_mem} GB ({used_mem} GB used)"

# This function retrieves disk information
def get_disk_info():
    # Get all disk partitions
    partitions = psutil.disk_partitions()
    
    # List to hold disk details
    disks = []
    
    for partition in partitions:
        # Skip non-existent or virtual devices if any
        try:
            # Get disk usage
            usage = psutil.disk_usage(partition.mountpoint)
            
            # Convert bytes to gigabytes
            total_disk = round(usage.total / (1024 * 1024 * 1024), 2)
            used_disk = round(usage.used / (1024 * 1024 * 1024), 2)
            
            # Append to disks list
            disks.append(f"{partition.device}: {total_disk} GB ({used_disk} GB used)")
        except:
            pass
    
    return "\n".join(disks)

# This function retrieves operating system information
def get_os_info():
    # Get OS name and version
    os_name = platform.system()
    os_arch = platform.architecture()
    os_version = platform.version()
    
    # Return formatted string
    return f"OS: {os_name} {os_arch} {os_version} "

# This function retrieves network interface information
def get_network_info():
    # Get all network interfaces with addresses
    interfaces = psutil.net_if_addrs()
    
    # List to hold IP details
    ips = []
    
    for interface, addrs in interfaces.items():
        # Check each address type (IPv4, IPv6)
        for addr in addrs:
            if addr.family == 2:  # IPv4
                ips.append(f"{interface}: {addr.address}")
    
    return "\n".join(ips)

# This function retrieves GPU information (Windows specific)
def get_gpu_info_windows():
    try:
        # Use WMI to query GPU info on Windows
        import win32com.client
        
        wmi = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        objWMIService = wmi.ConnectServer_()
        colItems = objWMIService.ExecQuery("SELECT * FROM Win32_DisplayControllerConfiguration")
        
        gpus = []
        for item in colItems:
            gpus.append(item.Caption)
        
        return "\n".join(gpus)
    except:
        return "GPU info not available"

# This function retrieves GPU information (macOS specific)
def get_gpu_info_mac():
    try:
        # Use system profiler to get GPU info on macOS
        output = subprocess.check_output(["system_profiler", "-xml", "SPDisplaysDataType"])
        
        # Parse the output for display information
        import plistlib
        
        sp = plistlib.loads(output)
        displays = sp[0]["_items"]
        
        gpus = []
        for display in displays:
            if "display_product" in display:
                gpus.append(display["display_vendor"] + " " + display["display_product"])
        
        return "\n".join(gpus)
    except:
        return "GPU info not available"

# Main function to gather and print all computer specifications
def main():

    # Clear the console (Windows only)
    if os.name == 'nt':
        subprocess.call('cls')
    
    # Print header
    print("\n" + "=" * 80)
    print("Computer Specifications")
    print("=" * 80 + "\n")

    # Get and print CPU info
    print("CPU:")
    print(get_cpu_info())
    print()

    # Get and print Memory info
    print("Memory:")
    print(get_memory_info())
    print()

    # Get and print Disk info
    print("Disks:")
    print(get_disk_info())
    print()

    # Get and print OS info
    print("Operating System:")
    print(get_os_info())
    print()

    # Get and print Network interfaces
    print("Network Interfaces:")
    print(get_network_info())
    print()

    # Get GPU info based on the OS
    if os.name == 'nt':
        print("GPU:")
        print(get_gpu_info_windows())
    elif os.name == 'posix' and platform.mac_ver()[0] != '':
        print("GPU:")
        print(get_gpu_info_mac())

# Check if being run as a script
if __name__ == "__main__":

    # Start measuring the processing time
    t1 = time.process_time()

    main()

    # Stop measuring the processing time
    t2 = time.process_time() 

    # Calculate the time difference
    time_diff = round(t2 - t1,8)

    # Print the total time taken to execute the program
    print("=" * 80 )
    print(f"It took {time_diff} Secs to generate this specs report")
    print("=" * 80 + "\n")