process = ["P1", "P2", "P3", "P4"]
at = [0, 2, 4, 6]   # Arrival Time
bt = [1, 3, 8, 6]   # Burst Time
n = len(process)
 
wt = [0] * n
tat = [0] * n
ct = [0] * n
 
# First process
ct[0] = at[0] + bt[0]
tat[0] = ct[0] - at[0]
wt[0] = tat[0] - bt[0]
 
# Remaining processes
for i in range(1, n):
    if ct[i-1] < at[i]:
        ct[i] = at[i] + bt[i]   # CPU Idle
    else:
        ct[i] = ct[i-1] + bt[i]
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]
 
# Display Table
print("Process\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(process[i], "\t", at[i], "\t", bt[i], "\t", ct[i], "\t", tat[i], "\t", wt[i])
 
print("\nAverage Waiting Time =", sum(wt) / n)
print("Average Turnaround Time =", sum(tat) / n)
 
# Gantt Chart
print("\nGantt Chart:")
time = 0
print(time, end="")
for i in range(n):
    if time < at[i]:
        print(f" --Idle-- {at[i]}", end="")
        time = at[i]
    print(f" --{process[i]}-- {ct[i]}", end="")
    time = ct[i]
print()


 
process = ["P1", "P2", "P3", "P4"]
at = [0, 2, 2, 5]   # Arrival Time
bt = [2, 4, 1, 2]   # Burst Time
n = len(process)
 
wt = [0] * n
tat = [0] * n
ct = [0] * n
completed = [False] * n
time = 0
completed_process = 0
gantt = []
 
while completed_process < n:
    shortest = -1
    min_bt = 999
    for i in range(n):
        if at[i] <= time and completed[i] == False:
            if bt[i] < min_bt:
                min_bt = bt[i]
                shortest = i
    if shortest == -1:
        gantt.append(("Idle", time))
        time += 1
        continue
    time = time + bt[shortest]
    ct[shortest] = time
    tat[shortest] = ct[shortest] - at[shortest]
    wt[shortest] = tat[shortest] - bt[shortest]
    completed[shortest] = True
    completed_process += 1
    gantt.append((process[shortest], time))
 
print("Process\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(process[i], "\t", at[i], "\t", bt[i],
          "\t", ct[i], "\t", tat[i], "\t", wt[i])
 
print("\nAverage Waiting Time =", sum(wt) / n)
print("Average Turnaround Time =", sum(tat) / n)
 
print("\nGantt Chart:")
start = 0
print(start, end="")
for p, end_time in gantt:
    print(f" --{p}-- {end_time}", end="")
print()

