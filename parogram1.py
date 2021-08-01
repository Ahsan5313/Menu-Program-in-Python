print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5 . Quit")


def add():
    num1 = int(input('Enter you number:'))
    num2 = int(input('Enter you number:'))
    print('Addition is {} '.format(num1 + num2))

def sub():
    num1 = int(input('Enter your number:'))
    num2 = int(input('Enter your number:'))
    print('Subtraction is {}'.format(num1 - num2))

def mul():
    num1 = int(input('Enter you number:'))
    num2 = int(input('Enter you number:'))
    print('Multiplication is {}'.format(num1 * num2))

def divf():
    try:
        num1 = int(input('Enter you number:'))
        num2 = int(input('Enter you number:'))
        print('Division is {}'.format(num1 / num2))
    except ZeroDivisionError as e:
        print(e)

try:
    choice = int(input('Enter a number 1 to 5:'))
except TypeError as e:
    print(e)


while True:

    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        divf()
    elif choice == 5:
        break


