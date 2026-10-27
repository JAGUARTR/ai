pages = [1, 2, 3, 1, 4, 5, 2, 1, 2, 3, 4, 5]
frames = 3
memory = []
page_faults = 0

for i in range(len(pages)):
    page = pages[i]
    if page not in memory:
        page_faults += 1
        if len(memory) < frames:
            memory.append(page)
        else:
            future = pages[i + 1:]
            index = -1
            farthest = -1
            for j in range(len(memory)):
                if memory[j] not in future:
                    index = j
                    break
                position = future.index(memory[j])
                if position > farthest:
                    farthest = position
                    index = j
            memory[index] = page
    print(page, "->", memory)

print("\nTotal Page Faults:", page_faults)
