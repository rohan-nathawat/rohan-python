BMI = float(input ("Enter the BMI value: "))

if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25.0: 
    print("Normal")
elif 25.0 <= BMI < 30.0: 
    print("Overweight")
else:
    print("Obese")