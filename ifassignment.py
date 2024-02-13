height =float(input("Enter height"))
weight =float(input("Enter weight"))

print("your BMI is", weight/height)

BMI=float("Enter your BMI:")

if BMI >= 5.0 and BMI <= 80:
    print("you are abnormal")
elif BMI >= 5.7 and BMI <= 100:
    print("you are normal")
elif BMI >= 6.4 and BMI <= 120:
    print("you are unhealthy")
elif BMI >= 6.8 and BMI <= 150:
    print("you are obese")
else:
    print("you are overweight")


