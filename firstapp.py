import psutil


def inf_cpu():
    infobox_cpu = {} 
    
    timebox_cpu = psutil.cpu_times()
    
    infobox_cpu.update(inf_user = timebox_cpu.user, 
    inf_sys = timebox_cpu.system, 
    inf_dle = timebox_cpu.idle,
    inf_count = psutil.cpu_count())
    
    freqbox_cpu = psutil.cpu_freq()
    infobox_cpu.update(freq_current = freqbox_cpu.current,
    freq_min = freqbox_cpu.min, 
    freq_max = freqbox_cpu.max)    

    return infobox_cpu() 

def inf_vmemory():
    infobox_vmemory = {}
    info_vmemory = psutil.virtual_memory()
    infobox_vmemory.update( total_vmemory = info_vmemory.total,
    used_vmemory = info_vmemory.used, free_vmemory = info_vmemory.free)

def inf_disks():
    infobox_disks = {}
    inf_disks = psutil.disk_usage('/')
    infobox_disks.update( inf_memory_total = inf_disks.total,
    inf_memory_used = inf_disks.used,
    inf_memory_free = inf_disks.free)
    






    



