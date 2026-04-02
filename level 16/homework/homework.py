# 2) 
numbers = []
for i in range(5):
    num = int(input("Enter number " + str(i+1) + ": "))
    numbers.append(num)

average = sum(numbers) / len(numbers)
print("Average:", average)

# 3) 
sentence = input("Enter a sentence: ")
print("Length of sentence:", len(sentence))

# 4) 
password = input("Enter your password: ")
if password.find('1') != -1:
    print("Password contains 1")
else:
    print("Password does not contain 1")

# 5) 
fruits = ['apple', 'banana', 'orange', 'mango']
fruits.append('cherry')          # add 'cherry' at end
fruits[3] = 'Blueberry'          # replace element at index 3
print(fruits)

# 6) 
word = input("Enter a word: ")
if word[0].isupper():
    print("Perfect")
else:
    print("Your word should be capitalized!")

# 7) 
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("Uppercase:", first_name.upper(), last_name.upper())
print("Lowercase:", first_name.lower(), last_name.lower())

# 8) 
my_name = "Alex"
user_name = input("Enter your name: ")

if my_name.lower() == user_name.lower():
    print("Our names are similar!")
else:
    print("We have different names")

# 9) 
my_string = "Sololearn"
letter = input("Enter a letter to find: ")
print("Index of letter:", my_string.find(letter))

# 10) 
words = ['apple', 'banana', 'cherry']
for i in range(len(words)):
    words[i] = words[i].upper()
print(words)

# 11) 
data = []
for i in range(3):
    value = input("Enter something: ")
    data.append(value)
print("List:", data)

# 12) 
fruits_list = ['apple', 'banana', 'orange', 'mango']
new_fruit = input("Enter a new fruit: ")
fruits_list.insert(2, new_fruit)
print("Updated fruits list:", fruits_list)