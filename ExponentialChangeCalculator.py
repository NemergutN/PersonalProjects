amount = float(input("Enter initial amount: "))
percentChange = float(input("Enter the percent change (without % sign): "))
compoundCount = int(input("Enter the amount of times it compounds: "))
newPercent = 1 + (percentChange * 0.01)
for i in range(compoundCount):
    amount = amount * newPercent
    print("The amount after " + str(i + 1) + " compound(s) is " + str(amount))