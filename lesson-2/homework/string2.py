# 2. Extract car names from this text: txt = 'LMaasleitbtui'

txt = 'LMaasleitbtui'
car_name1 = txt[::2] # Adashmasam "Lasetti" emas balki "Lacetti" kabi yoziladi
car_name2 = txt[1::2]
print(f"Car names are {car_name1} and {car_name2}")