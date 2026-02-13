from scheduler import Process,fcfs
processes=[
    Process(1, 0, 5),
    Process(2, 1, 3),
    Process(3, 2, 8),
    Process(4, 3, 6)
]
result=fcfs(processes)
print("FCFS result :",result)