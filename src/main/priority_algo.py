d = dict()
l = list()
print("Priority Algorithm ALGORITHM")
p = int(input("Enter Number Of Processes: "))

for i in range(p):
    at = int(input(f"Enter Arrival time of processes{i+1}: "))
    bt = int(input(f"Enter Burst time of process{i+1}: "))
    pr = int(input(f"Enter Priority of process{i+1}: "))
    d[f"p{i+1}"] = [at, bt, pr]
    
d = dict(sorted(d.items(), key=lambda item: (item[1][0], item[1][2], int(item[0][1:]))))
cur_time = 0
for i in range(p):
    if d[f"p{i+1}"][0] > cur_time:
        cur_time = d[f"p{i+1}"][0]
        
    ct = cur_time + d[f"p{i+1}"][1]
    d[f"p{i+1}"].append(ct)
    
    cur_time = ct
    
for i in range(p):
    tat = d[f"p{i + 1}"][3] - d[f"p{i + 1}"][0]
    d[f"p{i+1}"].append(tat)
    wt = d[f"p{i + 1}"][4] - d[f"p{i + 1}"][1]
    d[f"p{i+1}"].append(wt)
    
average_tat = sum(d[f"p{i+1}"][4] for i in range(p)) / p
average_wt = sum(d[f"p{i+1}"][5] for i in range(p)) / p

print(f"Process   ||   Arrival Time || Burst Time || priority        || Completion Time     || Turn Around Time || Wait Time")

for i in range(p):
    print(f"p{i+1:<8} || {d[f'p{i+1}'][0]:<14} || {d[f'p{i+1}'][1]:<12} || {d[f'p{i+1}'][2]:<15} || {d[f'p{i+1}'][3]:<19} || {d[f'p{i+1}'][4]:<16} || {d[f'p{i+1}'][4]:<16}")
