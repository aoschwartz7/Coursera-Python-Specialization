# this program will prompt for a score between 0.0 and 1.0 and will use
# Try/Except commands
score = float(input("Enter Score:"))
try:
        if score > 1.0:
            raise E()
        elif score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        else:
            print("F")
except:
    print("Please enter a score within the range 0 to 1.0")
    quit()
