#this program will use a function to return pay calculation

def computepay(hr, pay):
    hr = int(hr)
    if hr > 40:
        hr = (hr - 40) * 1.5
        hr = hr + 40
    paycheck = float(hr) * float(pay)
    return paycheck
hr = input("Hours: ")
pay = input("Hourly Rate: ")
print(computepay(hr, pay))
