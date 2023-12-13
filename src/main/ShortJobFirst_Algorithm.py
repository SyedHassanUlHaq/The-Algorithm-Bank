d = dict()
l = list()
print("SHORT JOB FIRST ALGORITHM")
p = int(input("Enter Number Of Processes: "))

for i in range(p):
    at = int(input(f"Enter Arrival time of processes{i+1}: "))
    bt = int(input(f"Enter Burst time of process{i+1}: "))
    d[f"p{i+1}"] = [at, bt]
    
d = dict(sorted(d.items(), key=lambda item: item[1][1]))

for i in range(p):
    Arrivaltime = d[f"p{i+1}"][0]
    Bursttime = d[f"p{i+1}"][1]
    ct = Arrivaltime + Bursttime
    d[f"p{i+1}"].append(ct)
    Completiontime = d[f"p{i+1}"][2]
    tat = Completiontime - Arrivaltime
    d[f"p{i+1}"].append(tat)
    TurnAroundtime = d[f"p{i+1}"][3]
    wt = TurnAroundtime - Bursttime
    d[f"p{i+1}"].append(wt)


average_tat = sum(d[f"p{i+1}"][3] for i in range(p)) / p
average_wt = sum(d[f"p{i+1}"][4] for i in range(p)) / p
print(f"Process || Arrival Time || Burst Time || Completion Time || Turn Around Time || Wait Time")
for i in range(p):
    print(f"p{i+1:<8} || {d[f'p{i+1}'][0]:<14} || {d[f'p{i+1}'][1]:<12} || {d[f'p{i+1}'][2]:<18} || {d[f'p{i+1}'][3]:<19} || {d[f'p{i+1}'][4]:<12}")

    
print(f"AVERAGE Turn Around Time is: {average_tat}")
print(f"AVERAGE Wait Time is: {average_wt}")