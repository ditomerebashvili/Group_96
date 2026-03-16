num = int(input("Enter a number: "))  #პირველი დავალება
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")






password = "dito123"  #მეორე



while True:
    user = input("Enter password: ")

    if user == password:
        print("Access granted")
        break
    else:
        print("wrong password,try again")


fruits = ["banana" , "apple" , "orange" , "mango" , "cherry"] #მესამე
print(fruits[1])
print(fruits[2])
print(fruits[4])