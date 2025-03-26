def convert_cel_to_far(cel):
    return cel * 9/5 +32
def convert_far_to_cel(far):
    return (far - 32) * 5/9
def main():
    temp_cel = float(input("Enter a temperature in degrees C: "))
    temp_far = convert_cel_to_far(temp_cel)
    print(f"{temp_cel: .0f} degrees C = {temp_far: .2f} deegres F")
    temp_far = float(input("Enter a temperature in deegres F: "))
    temp_cel = convert_far_to_cel(temp_far)
    print(f"{temp_far: .0f} deegres F = {temp_cel: .2f} deegres C")

if __name__ == "__main__":
    main()