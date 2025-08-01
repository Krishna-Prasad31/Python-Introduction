principal = float(input("What is the Principal amount?"))
tenure = float(input("What is the tenure in years?"))
rate = float(input("What is the rate"))

result = (principal*tenure*rate)/100

print("Your Simple Interest is: " + str(result))