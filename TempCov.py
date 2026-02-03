def ToCelsius(TempF):
    """Convert Fahrenheit to Celsius"""
    return (TempF - 32) * 5.0/9.0

def ToFahrenheit(TempC):
    """Convert Celsius to Fahrenheit"""
    return TempC * 9.0/5.0 + 32

f_Temp = 100.0
c_Temp = ToCelsius(f_Temp)
print(f"{f_Temp} degrees Fahrenheit is {c_Temp} degrees Celsius.")

c_Temp = 0.0
f_Temp = ToFahrenheit(c_Temp)   
print(f"{c_Temp} degrees Celsius is {f_Temp} degrees Fahrenheit.")