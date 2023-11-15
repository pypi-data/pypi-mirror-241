""" Detect machine cpu, rams, space. GPU availability. TF and torch availability"""

def detect_board():
    import platform

    import psutil
    import platform
    #from datetime import datetime
    import cpuinfo
    cpufreq = psutil.cpu_freq()

    mem = psutil.virtual_memory()
    info1 =  {"machine" : platform.machine(),
            "version" : platform.version(),
            "uname"   : platform.uname(),
            "system"  : platform.system(),
            "processor": platform.processor(),
            "ram" :  mem.total ,
            #"ram_GB"     : str(round(total_ram / (1024.0 **3)))+" GB",
            "ram_free" : mem.available,
            "cpu_cores_physical": psutil.cpu_count(logical=False),
            "cpu_cores": psutil.cpu_count(logical=True),
            "cpu_freq_max": cpufreq.max,
            #"cpu_freq_min": cpufreq.min,


            }
    info1.update(cpuinfo.get_cpu_info())
    return info1
print(detect_board())
