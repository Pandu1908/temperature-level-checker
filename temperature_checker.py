temperature = float(input("Enter temperature in °C: "))

if temperature < 20:
    print("Temperature: LOW")
elif temperature <= 35:
    print("Temperature: NORMAL")
else:
    print("Temperature: HIGH")
