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
        shortest=min(available,key=lambda x:(x.bur_time,x.arri_time))
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

from collections import deque
def rr(processes,quantum=2):
    processes=sorted(processes,key=lambda x:(x.arri_time,x.pid))
    n=len(processes)
    remaining_bt={p.pid:p.bur_time for p in processes}
    queue=deque()
    current_time=0
    completion_time={}
    i=0
    while queue or i<n:
        while i<n and processes[i].arri_time<=current_time:
            queue.append(processes[i])
            i+=1
        if not queue:
            current_time=processes[i].arri_time
            continue
        process=queue.popleft()
        execution_time=min(quantum,remaining_bt[process.pid])
        remaining_bt[process.pid]-=execution_time
        current_time+=execution_time
        while i<n and processes[i].arri_time<=current_time:
            queue.append(processes[i])
            i+=1
        if remaining_bt[process.pid]>0:
            queue.append(process)
        if remaining_bt[process.pid]==0:
            completion_time[process.pid]=current_time
    total_tat=0
    total_wt=0
    for p in processes:
        tat=completion_time[p.pid]-p.arri_time
        wt=tat-p.bur_time
        total_tat+=tat
        total_wt+=wt
    return{
    "average_wt":total_wt/n,
    "average_tat":total_tat/n
    }