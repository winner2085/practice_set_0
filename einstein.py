#Create a program that calulate E=MC2 round (kg *(300000000) ** 2)

def main():
    mass = float(input("Type a number: "))
    convert(mass)

def convert(kg):
    converted_kg = round(kg * (300000000 ** 2))
    print(f"{converted_kg}:.0f")


main()