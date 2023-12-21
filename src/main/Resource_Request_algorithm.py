def is_safe_state(available, request, allocation):
    processes = len(allocation)
    resources = len(available)

    work = available.copy()
    finish = [False] * processes

    need = [[request[i][j] - allocation[i][j] for j in range(resources)] for i in range(processes)]

    for i in range(processes):
        if not finish[i] and all(request[i][j] <= need[i][j] and request[i][j] <= available[j] for j in range(resources)):
            for j in range(resources):
                available[j] -= request[i][j]
                allocation[i][j] += request[i][j]
                need[i][j] -= request[i][j]

            finish[i] = True

    if all(finish):
        print("System is in a safe state.")
        return True
    else:
        print("System is NOT in a safe state.")
        return False

# Example Usage
available_resources = [3, 3, 2]
request = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

is_safe_state(available_resources, request, allocation)

