name = input("Enter file:")
try:
    handle = open(name)
except:
    print(f'cannot open file: {name}')
hours = dict()
for line in handle: 
    if line.startswith("From "):
        hour = line.split()[5].split(':')[0]
        hours[hour] = hours.get(hour, 0) + 1 
for k, v in sorted(hours.items()):
    print(k, v)