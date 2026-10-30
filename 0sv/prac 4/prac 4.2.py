#sjf
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
