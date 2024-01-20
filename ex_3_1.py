hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = 0

if hrs > 40:
    pay += 40 * rate
    pay += (hrs - 40) * rate * 1.5 
else: 
    pay += hrs * rate 

print(pay)