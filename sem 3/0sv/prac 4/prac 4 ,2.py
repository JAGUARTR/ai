process = ["P1", "P2", "P3", "P4"]
at = [0, 2, 3, 5]
bt = [7, 4, 1, 2]
priority = [2, 1, 4, 2]
n = len(process)
 
wt = [0] * n
tat = [0] * n
ct = [0] * n
completed = [False] * n
time = 0
count = 0
gantt = []
 
while count < n:
    highest = -1
    min_priority = 999
    for i in range(n):
        if at[i] <= time and completed[i] == False:
            if priority[i] < min_priority:
                min_priority = priority[i]
                highest = i
    if highest == -1:
        gantt.append(("Idle", time))
        time += 1
        continue
    time += bt[highest]
    ct[highest] = time
    tat[highest] = ct[highest] - at[highest]
    wt[highest] = tat[highest] - bt[highest]
    completed[highest] = True
    count += 1
    gantt.append((process[highest], time))
 
print("Process\tAT\tBT\tPriority\tCT\tTAT\tWT")
for i in range(n):
    print(process[i], "\t", at[i], "\t", bt[i], "\t",
          priority[i], "\t\t", ct[i], "\t", tat[i], "\t", wt[i])
 
print("\nAverage Waiting Time =", sum(wt) / n)
print("Average Turnaround Time =", sum(tat) / n)
 
print("\nGantt Chart:")
time = 0
print(time, end="")
for p, end_time in gantt:
    print(f" --{p}-- {end_time}", end="")
print()
