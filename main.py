newlist = []
def sumador():
    while True:
        try:
            a = int(input('Enter a number (To finish, enter a string): '))
            newlist.append(a)
        except ValueError:
            print(f"suma de todos {sum(newlist)}")
            break
sumador()