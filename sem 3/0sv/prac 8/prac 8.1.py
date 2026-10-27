pages = [1, 2, 3, 1, 4, 5, 2, 1, 2, 3, 4, 5]
frames = 3
memory = []
page_faults = 0

for page in pages:
    if page not in memory:
        page_faults += 1
        if len(memory) < frames:
            memory.append(page)
        else:
            memory.pop(0)
            memory.append(page)
    print(page, "->", memory)

print("\nTotal Page Faults:", page_faults)
