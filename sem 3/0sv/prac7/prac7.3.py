#worst fit
blocks = [20, 100, 40, 200, 10]
processes = [90, 50, 30, 40]

allocation = [-1] * len(processes)

for i in range(len(processes)):
    worst = -1
    for j in range(len(blocks)):
        if blocks[j] >= processes[i]:
            if worst == -1 or blocks[j] > blocks[worst]:
                worst = j
    if worst != -1:
        allocation[i] = worst
        blocks[worst] -= processes[i]

print("Process\tSize\tBlock")
for i in range(len(processes)):
    if allocation[i] != -1:
        print(f"P{i+1}\t{processes[i]}\tBlock {allocation[i]+1}")
    else:
        print(f"P{i+1}\t{processes[i]}\tNot Allocated")
