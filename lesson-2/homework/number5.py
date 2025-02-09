# 5. Make a program that converts a given Celsius temperature to Fahrenheit.

weather_in_c = input("Please enter degree: ")
convert_to_f = float(weather_in_c) * 33.8
convert_to_f_round = round(convert_to_f, 1)
print(f"{weather_in_c} celsius equal to {convert_to_f_round} fahrenheit")