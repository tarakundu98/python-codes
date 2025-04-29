unit=input("Enter the unit of temperature (C/F): ")
t=float(input("Enter temperature : "))
if unit=="C" :
    tf=round(t*9/5+32,2)
    print(f"Temp. in Fahrenheit = {tf}")
elif unit=="F" :
    tc=round((t-32)*5/9,2)
    print(f"Temp. in Celsius = {tc}")