# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try: 
    fh = open(fname)
except: 
    print("cannot open file: {}".format(fname))
    quit()
occurrences = 0
total_confidence = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    total_confidence += float((line.rstrip()[20:]))
    occurrences += 1
print("Average spam confidence: {}".format(total_confidence/occurrences))
