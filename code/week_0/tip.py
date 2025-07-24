def tips():
    rand = float(input("R:"))
    percent = float(input("tip percentaage:"))
    tip = rand * (percent/100)
    print(f"leave R{tip: .2f}")
tips()