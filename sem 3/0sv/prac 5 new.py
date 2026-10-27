allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]
 
maximum = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
 
available = [3, 3, 2]
 
n = 5
m = 3
 
# Calculate Need Matrix
need = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(maximum[i][j] - allocation[i][j])
    need.append(row)
 
print("Need Matrix:")
for i in range(n):
    print("P", i, ":", need[i])
 
# Safety Algorithm
work = available[:]
finish = [False] * n
safe = []
 
while len(safe) < n:
    found = False
    for i in range(n):
        if not finish[i]:
            possible = True
            for j in range(m):
                if need[i][j] > work[j]:
                    possible = False
                    break
            if possible:
                for j in range(m):
                    work[j] += allocation[i][j]
                finish[i] = True
                safe.append(i)
                found = True
    if not found:
        break
 
if len(safe) == n:
    print("\nSystem is in Safe State")
    print("Safe Sequence:", end=" ")
    for p in safe:
        print("P" + str(p), end=" ")
else:
    print("\nSystem is NOT in Safe State")
 
# ---------------- Additional Resource Request ----------------
print("\n\nAdditional Resource Request")
process = int(input("Enter Process Number: "))
request = list(map(int, input("Enter Request (3 values): ").split()))
 
grant = True
 
# Check Request <= Need
for i in range(m):
    if request[i] > need[process][i]:
        print("Request exceeds Need.")
        grant = False
        break
 
# Check Request <= Available
if grant:
    for i in range(m):
        if request[i] > available[i]:
            print("Resources are not available.")
            grant = False
            break
 
if grant:
    print("Request can be granted immediately.")
else:
    print("Request cannot be granted.")
