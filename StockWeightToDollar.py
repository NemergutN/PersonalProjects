dollars = int(input("Enter dollar amount: "))
while True:
    try:
        symbol, weight = input("Enter stock and weight: ").split()
        print("Money on " + symbol + ": " + str(float(weight) * dollars))
    except EOFError:
        break