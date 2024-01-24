name = input("Enter file:")

try: 
    fhand = open(name)
except: 
    print('cannot open file: {}'.format(name))
    quit()

sender_count = {}
for line in fhand: 
    if line.startswith('From '):
        sender_count[line.rstrip().split()[1]] = sender_count.get(line.rstrip().split()[1], 0) + 1

highest_name = None
highest_count = None
for name, count in sender_count.items():
    if highest_name is None: 
        highest_name = name
        highest_count = count
        continue
    if count > highest_count: 
        highest_name = name
        highest_count = count

print(highest_name, highest_count)