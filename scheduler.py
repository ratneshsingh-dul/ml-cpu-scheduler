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
