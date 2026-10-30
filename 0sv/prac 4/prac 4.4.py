#round robin
process = ["P1", "P2", "P3", "P4"]
at = [0, 1, 3, 5]
bt = [5, 4, 2, 6]
tq = 2
n = len(process)
 
rt = bt[:]
ct = [0] * n
tat = [0] * n
wt = [0] * n
queue = []
visited = [False] * n
time = 0
completed = 0
gantt = []
 
queue.append(0)
visited[0] = True
 
while completed < n:
    if len(queue) == 0:
        gantt.append(("Idle", time))
        time += 1
        for i in range(n):
            if at[i] <= time and not visited[i]:
                queue.append(i)
                visited[i] = True
        continue
 
    i = queue.pop(0)
    if rt[i] > tq:
        time += tq
        rt[i] -= tq
    else:
        time += rt[i]
        rt[i] = 0
        ct[i] = time
        completed += 1
    gantt.append((process[i], time))
 
    for j in range(n):
        if at[j] <= time and not visited[j]:
            queue.append(j)
            visited[j] = True
    if rt[i] > 0:
        queue.append(i)
 
for i in range(n):
    tat[i] = ct[i] - at[i]
    wt[i] = tat[i] - bt[i]
 
print("Process\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    print(process[i], "\t", at[i], "\t", bt[i], "\t",
          ct[i], "\t", tat[i], "\t", wt[i])
 
print("\nAverage WT =", sum(wt) / n)
print("Average TAT =", sum(tat) / n)
 
print("\nGantt Chart:")
print("0", end="")
for p, t in gantt:
    print(f" --{p}-- {t}", end="")
print()
