# 3. Create a program that converts kilometers to meters and centimeters.

length = input('Create length: ')
length_in_km  = float(length)
convert_to_m  = str(length_in_km * 10e2).split(".")[0]
convert_to_cm = str(length_in_km * 10e4).split(".")[0]
print(f"{length_in_km} km is equal to  {convert_to_m}  meter")
print(f"{length_in_km} km is equal to {convert_to_cm} centimeter")