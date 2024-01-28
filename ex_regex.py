import re

name = input("Enter file:")
try:
    handle = open(name)
except:
    print(f'cannot open file: {name}')
numbers_array = list()
for line in handle: 
    numbers_array += [int(number) for number in re.findall('\d+', line)] 
print(sum(numbers_array))