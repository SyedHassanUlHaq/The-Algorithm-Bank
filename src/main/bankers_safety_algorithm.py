def is_safe_state(available, max_claim, allocation):
    processes = len(allocation)
    resources = len(available)
    
    work = available.copy()
    finish = [False] * processes

    need = [[max_claim[i][j] - allocation[i][j] for j in range (resources)] for i in range(processes)]

    for i in range(processes):
        for j in range(resources):
            if need[i][j] <= work[j]:
                work[j] + allocation[i][j]
                finish[i] = True
            else:
                finish[i] = True

    return all(finish)
available_resources = [3, 3, 2]
max_claim = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

if is_safe_state(available_resources, max_claim, allocation):
    print("The system is in a safe state.")
else:
    print("The system is NOT in a safe state.")
