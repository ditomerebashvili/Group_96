number = int(input("შემოიტანეთ რიცხვი: "))  #შემოწმება ლუწია თუ კენტია შემოტანილი რიცხვი
if number % 2 == 0:
    print("ლუწია")
else:
    print("კენტია")




temp = float(input("შეიყვანეთ ტემპერატურა: "))  #ტემპერატურის შემოწმება
if temp > 30:
    print("It's Hot")
elif 15 <= temp <= 30:
    print("It's Warm")
else:
    print("It's Cold")



num = int(input("შემოიტანეთ რიცხვი: "))  #რიცხვის ტიპის შემოწმება
if num < 0:
    print("Negative")
elif num > 0:
    if num % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
else:
    print("რიცხვი არის ნული")



limit = int(input("შეიყვანეთ რიცხვი: "))    
for i in range(limit + 1):
    if i % 2 == 0:
        print(f"{i} - Even")
    else:
        print(f"{i} - Odd")




positive = 0  
negative = 0
zero = 0

for i in range(10):
    n = int(input(f"შეიყვანეთ მე-{i+1} რიცხვი: "))   #რიცხვების შემოწმება
    if n > 0:
        positive += 1
    elif n < 0:
        negative += 1
    else:
        zero += 1

print(f"დადებითი: {positive}, უარყოფითი: {negative}, ნული: {zero}")




fruits = ["apple", "banana", "orange", "grape"]
fruits[1] = "kiwi" # ბანანი არის მეორე ელემენტი (ინდექსი 1)
print(fruits)




nums = [4, 8, 12, 16, 20]
result = nums[0] + nums[-1]
print("შედეგი:", result)







my_list = [2, 5, 8, 10, 3, 15, 4, 7]

# 10. თითოეული წევრის დაბეჭდვა
print("ყველა წევრი:")
for x in my_list:
    print(x)

# 11. მხოლოდ ლუწი რიცხვები
print("ლუწი რიცხვები:")
for x in my_list:
    if x % 2 == 0:
        print(x)

# 12. ლუწი რიცხვების ჯამი
even_sum = sum(x for x in my_list if x % 2 == 0)
print("ლუწების ჯამი:", even_sum)

# 13. რიცხვები, რომლებიც მეტია 6-ზე
print("6-ზე მეტი რიცხვები:")
for x in my_list:
    if x > 6:
        print(x)




items = ["ა", "ბ", "გ", "დ", "ე"]
print(items[:3])