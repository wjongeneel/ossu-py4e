fname = input("Enter file name: ")
try: 
    fh = open(fname)
except: 
    print('cannot open file: {}'.format(fname))
    quit()
lst = list()
for line in fh:
    for word in line.rstrip().split(): 
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
