import psutil




def inf_cpu():
    infobox_cpu = {} 
    
    timebox_cpu = psutil.cpu_times()
    
    infobox_cpu.update(inf_user = timebox_cpu.user, 
    inf_sys = timebox_cpu.system, 
    inf_dle = timebox_cpu.idle)
    
    freqbox_cpu = psutil.cpu_freq()
    infobox_cpu.update(freq_current = freqbox_cpu.current,
    freq_min = freqbox_cpu.min, 
    freq_max = freqbox_cpu.max)    

    return infobox_cpu

def inf_vmemory():
    infobox_vmemory = {}
    info_vmemory = psutil.virtual_memory()
    infobox_vmemory.update( total_vmemory = info_vmemory.total,
    used_vmemory = info_vmemory.used, 
    free_vmemory = info_vmemory.free)
    return infobox_vmemory

def inf_disks():
    infobox_disks = {}
    inf_disks = psutil.disk_usage('/')
    infobox_disks.update( inf_memory_total = inf_disks.total,
    inf_memory_used = inf_disks.used,
    inf_memory_free = inf_disks.free)
    return infobox_disks
    
def show_cpu(infobox_cpu):
    date_cpu = infobox_cpu.items()
    stq1 = 'Time spent by normal processes executing in user mode :{}'.format(date_cpu[2])


def show_cpu_count():
    print('Count CPU: {}\n'.format(psutil.cpu_count()))

def show_cpu(infobox_cpu):
    date_cpu = list(infobox_cpu.values())
    user = str(date_cpu[0])
    system = str(date_cpu[1])
    idle = str(date_cpu[2])
    current = str(date_cpu[3])
    min = str(date_cpu[4])
    max = str(date_cpu[5])
    print('_____________________________________________________________________ \n')
    print(
    'CPU: \nTime spent by normal processes executing in user mode: |\t {} \n'
    'Time spent by processes executing in kernel mode:      |\t {} \n'
    'Time spent doing nothing:                              |\t {} \n'
    'CPU frequency:                                         |\t {} \n'
    'CPU frequency MIN:                                     |\t {} \n'
    'CPU frequency MAX:                                     |\t {} \n'
    .format(user, system, idle, current,min, max))
    print('_____________________________________________________________________ \n')

def show_vmemory(infobox_vmemory):
    date_vmemory = list(infobox_vmemory.values())
    total = str(date_vmemory[0])
    used = str(date_vmemory[1])
    free = str(date_vmemory[1])
    
    print('Vmemory:_______________________________________________| \n'
    'Total:|________________________________________________|\t {} \n'
    'Used: |________________________________________________|\t {} \n'
    'Free: |________________________________________________|\t {} \n'
    .format(total,used,free))
    print('_____________________________________________________________________ \n')

def show_disks(infobox_disks):
    date_disks = list(infobox_disks.values())
    total = str(date_disks[0])
    used = str(date_disks[1])
    free = str(date_disks[1])
    print(
    'Disks: ________________________________________________\n'
    'Total:|________________________________________________|\t {} \n'
    'Used: |________________________________________________|\t {} \n'
    'Free: |________________________________________________|\t {} \n'
    .format(total,used,free))
    print('_____________________________________________________________________ \n')




show_cpu_count()

date_cpu = inf_cpu()
show_cpu(date_cpu)

date_vmemory = inf_vmemory()
show_vmemory(date_vmemory)

date_disks = inf_disks()
show_disks(date_disks)






    



