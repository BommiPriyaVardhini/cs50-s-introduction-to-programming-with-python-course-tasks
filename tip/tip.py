def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d=d[1:]
    x=float(d)
    return x

def percent_to_float(p):
    p=p[:-1]
    p=float(p)/100
    return p
main()
