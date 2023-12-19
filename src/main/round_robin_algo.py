def round_robin(processes, quantum):
    n = len(processes)
    remaining_burst_time = [process['burst_time'] for process in processes]
    completion_time = [0] * n
    turn_around_time = [0] * n
    wait_time = [0] * n
    time = 0

    print(f"Process   ||   Arrival Time || Burst Time || Quantum time        || Completion Time     || Turn Around Time || Wait Time")
    print("=" * 115)

    while True:
        done = True
        for i in range(n):
            if remaining_burst_time[i] > 0:
                done = False

                if remaining_burst_time[i] > quantum:
                    print(f"{processes[i]['name']:^10} || {processes[i]['arrival_time']:^15} || {processes[i]['burst_time']:^11} || {quantum:^20} || {time + quantum:^20} || {time + quantum - processes[i]['arrival_time']:^18} || {time - processes[i]['arrival_time']:^11}")
                    remaining_burst_time[i] -= quantum
                    time += quantum
                else:
                    print(f"{processes[i]['name']:^10} || {processes[i]['arrival_time']:^15} || {processes[i]['burst_time']:^11} || {remaining_burst_time[i]:^20} || {time + remaining_burst_time[i]:^20} || {time + remaining_burst_time[i] - processes[i]['arrival_time']:^18} || {time - processes[i]['arrival_time']:^11}")
                    time += remaining_burst_time[i]
                    remaining_burst_time[i] = 0

        if done:
            break

if __name__ == "__main__":
    processes = [
        {"name": "P1", "arrival_time": 0, "burst_time": 5},
        {"name": "P2", "arrival_time": 1, "burst_time": 9},
        {"name": "P3", "arrival_time": 2, "burst_time": 3},
    ]

    time_quantum = 2

    round_robin(processes, time_quantum)

