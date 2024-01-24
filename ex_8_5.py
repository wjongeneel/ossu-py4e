fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('cannot open file: {}'.format(fname))
    quit()
count = 0
for line in fh:
    if line.startswith('From '):
        print(line.rstrip().split()[1])
        count += 1
print("There were {} lines in the file with From as the first word".format(count))
