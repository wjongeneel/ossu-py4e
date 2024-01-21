largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try: 
        if largest == None:
            largest = int(num)
        elif int(num) > largest:
            largest = int(num)
        else: 
            pass 
        if smallest == None: 
            smallest = int(num)
        elif int(num) < smallest: 
            smallest = int(num)
        else:
            pass
    except: 
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)