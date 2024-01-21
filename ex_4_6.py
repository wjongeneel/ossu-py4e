def computepay(h, r):
    pay = 0
    if h > 40:
        pay += 40 * r
        pay += (h - 40) * r * 1.5 
    else: 
        pay += h * r
    return pay

hrs = float(input("Enter Hours:\n"))
rate = float(input("Enter Rate:\n"))

p = computepay(hrs, rate)
print("Pay " + str(p))