total_time = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0

for i in total_time.split(','):
    for k in i.split(' '):
        if 'h' in k:
            h = k.replace('h', '')
            total_minutes += int(h) * 60
        elif 'm' in k:
            m = k.replace('m', '')
            total_minutes += int(m)
        elif "s" in k:
            s = k.replace('s', '')
            total_minutes += int(s) // 60

print(total_minutes)
