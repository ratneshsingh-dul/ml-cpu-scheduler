from scheduler import Process,fcfs,sjf,rr
processes = [
    Process(1, 0, 5, priority=2),
    Process(2, 1, 3, priority=1),
    Process(3, 2, 8, priority=4),
    Process(4, 3, 6, priority=3)
]

print("FCFS result :",fcfs(processes))
print("SJF result :",sjf(processes))
print("Round Robin result :",rr(processes,5))
