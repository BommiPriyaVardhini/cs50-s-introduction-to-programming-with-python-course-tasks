def main():
    weight=float(input("Enter your weight in (lbs): "))
    height=float(input("Enter your height in (inches): "))
    height_converted=convert_height(height)
    pounds_converted=calculate_weight(weight)
    bmi=weight/(height**2)*703
    print(f"Your Earth BMI is:{bmi:.2F}")

    print()
    weightonMoon=round((weight*1.622)/9.81,2)
    moonpounds=weightonMoon*2.205
    print(f"But you are only {moonpounds:.2f} pounds on the moon ")
def convert_height(n2):
    h2=float(n2**2)
    return h2
def calculate_weight(n1):
    w=int(n1)
    return w
def cal_bmi(n3):
    bmi=round(n3)
    return bmi
if __name__ ="__main__":
    main()
