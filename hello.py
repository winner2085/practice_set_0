"""#Ask user for name
name = input("What is your name? ")

#Remove whitespace
name = name.strip()

#Capitalize user name
name = name.title()

#Say hello
print(f"Hello, {name}")"""


"""#simplified
name = input("What is your name? ").strip().title()
print(f"Hello, {name}")"""


"""name = input("What is your name? ").strip().title()

def hello():
    print(f"Hello, {name}")

hello()"""

def main():
    name = input("What is your name? ").strip().title()
    hello(name)

def hello(user_name):
    print(f"Hello, {user_name}")


main()