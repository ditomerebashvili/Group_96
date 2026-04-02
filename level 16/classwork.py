word = input("Enter your name: ")  #2 davaleba
letter = input("Enter one letter: ")

print(word.find(letter))



fruits = ['apple','banana','peach','pineapple']  #3 davaleba

fruits.append('orange')
fruits.append('grape')
fruits.append('mango')

print(len(fruits))


word1 = input("Enter your name: ")  #1 davaleba

if word1.isupper():
    print("სიტყვა დაწყებულია დიდი ასოთი")
else:
    print("სიტყვა არ არის დიდი ასოთი დაწყებული")