print("!Calculator!")
while True:
    try:
        number_one = int(input("Choice first number: "))
        number_two = int(input("Choice second number: "))
        break
    except ValueError:
        print("Error: please, use ONLY numbers!")
print("1 - *")
print("2 - /")
print("3 - +")
print("4 - -")
while True:
    try:
        action = int(input("Choice the action (1, 2, 3 or 4): "))
        if action in[1, 2, 3, 4]:
            break  
        else:
            print("Error: please, use numbers FROM 1 TO 4!")
    except ValueError:
        print("Error: please, use ONLY numbers!")
if action == 1:
    print("Result: ", number_one * number_two)
elif action == 2:
    print("Result: ", number_one / number_two)
elif action == 3:
    print("Result: ", number_one + number_two)
elif action == 4:
    print("Result: ", number_one - number_two)
print("-" * 30)
