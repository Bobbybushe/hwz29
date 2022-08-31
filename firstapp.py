import psutil


   

def inf_cpu():
    infobox_cpu = {} 
    infobox_cpu.update(
    inf_cpu_count = psutil.cpu_count())
    freqbox_cpu = psutil.cpu_freq()
    infobox_cpu.update(
    freq_current = freqbox_cpu.current,
    freq_min = freqbox_cpu.min, 
    freq_max = freqbox_cpu.max
    )
    infobox_cpu.update(cpu_usage = psutil.cpu_percent(interval=1))
    return infobox_cpu

def inf_vmemory():
    infobox_vmemory = {}
    info_vmemory = psutil.virtual_memory()
    infobox_vmemory.update(
    total_vmemory = info_vmemory.total, 
    used_vmemory = info_vmemory.used, 
    free_vmemory = info_vmemory.free
    )
    return infobox_vmemory

def inf_disks():
    infobox_disks = {}
    inf_disks = psutil.disk_usage('/')
    infobox_disks.update(
    inf_memory_total = inf_disks.total,
    inf_memory_used = inf_disks.used,
    inf_memory_free = inf_disks.free
    )
    return infobox_disks
    

def show_cpu(infobox_cpu):
    date_cpu = list(infobox_cpu.values())
    print(
    'CPU: \n'
    'CPU count:          \t {} cores\n'
    'CPU frequency:    \t {} MHz \n'
    'CPU frequency MIN:\t {} MHz\n'
    'CPU frequency MAX:\t {} MHz\n'
    'CPU usage:        \t {} %\n'

    .format(date_cpu[0], date_cpu[1],date_cpu[2], date_cpu[3],date_cpu[4]))
  

def show_vmemory(infobox_vmemory):
    date_vmemory = list(infobox_vmemory.values())   
    print('Virtual memory: \n'
    'Total:\t {} bytes\n'
    'Used: \t {} bytes\n'
    'Free: \t {} bytes\n'
    .format(date_vmemory[0],date_vmemory[1],date_vmemory[1]))
  

def show_disks(infobox_disks):
    date_disks = list(infobox_disks.values())
    print(
    'Disks memory:\n'
    'Total:\t {} bytes\n'
    'Used: \t {} bytes\n'
    'Free: \t {} bytes\n'
    .format(date_disks[0],date_disks[1],date_disks[1]))

def show_processes():
    print('Processes:\n')
    for proc in psutil.process_iter(['pid','name','username']):
        print(proc.info)




date_cpu = inf_cpu()
show_cpu(date_cpu)
date_vmemory = inf_vmemory()
show_vmemory(date_vmemory)
date_disks = inf_disks()
show_disks(date_disks)
show_processes()