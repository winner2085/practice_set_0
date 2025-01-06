def main():
    color = input("Give a color: ").casefold()
    user(color)

def user(your_color):
    print(f"Your color is: {your_color}")

main()