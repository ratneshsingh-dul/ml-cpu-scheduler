class Process:
    def __init__(self,pid,arri_time,bur_time,priority=0):
        self.pid=pid
        self.arri_time=arri_time
        self.bur_time=bur_time
        self.priority=priority
    
def fcfs(processes):
    processes=sorted(processes,key=lambda x:x.arri_time)
    current_time=0
    total_wt=0
    total_tat=0
    for process in processes:
        if current_time<process.arri_time:
            current_time=process.arri_time
        wt=current_time-process.arri_time
        tat=wt+process.bur_time
        total_wt+=wt
        total_tat+=tat
        current_time+=process.bur_time
    n=len(processes)
    return{
    "average_wt":total_wt/n,
    "average_tat":total_tat/n
    }

def sjf(processes):
    process_copy=processes.copy()
    current_time=0
    total_wt=0
    total_tat=0
    completed=[]
    n=len(processes)
    while process_copy:
        available=[]
        for i in process_copy:
            if i.arri_time<=current_time:
                available.append(i)
        if not available:
            current_time=min(p.arri_time for p in process_copy)
            continue
        shortest=min(available,key=lambda x:x.bur_time)
        wt=current_time-shortest.arri_time
        tat=wt+shortest.bur_time
        total_wt+=wt
        total_tat+=tat
        current_time+=shortest.bur_time
        completed.append(shortest)
        process_copy.remove(shortest)
    return{
    "average_wt":total_wt/n,
    "average_tat":total_tat/n
    }
