BMI = float(input ("Enter the BMI value: "))

if 0 < BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25.0: 
    print("Normal")
elif 25.0 <= BMI < 30.0: 
    print("Overweight")
elif BMI > 30.0:
    print("Obese")
else:
    print("Invaild BMI Value")