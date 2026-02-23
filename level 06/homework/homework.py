#type() ფუნქცია აბრუნებს ობიექტის/ცვლადის მონაცემთა ტიპს (data type).
#ანუ გვიჩვენებს, თუ რა ტიპის მნიშვნელობა ინახება ცვლადში — int, float, str, bool და ა.შ.

name = "dito"
surname = "merebashvili"
age = 15 
#print("I am " + name + " " + surname + " and I am " + age + " years old")  #დააბრუნებს errors ვინაიდან კონკატინაცია ვერ განხორციელდება string სა და integer-ს შორის
#გასწორებული ვერსია იქნება
print("I am " + name + " " + surname + " and I am " + str(age) + " years old") #გამოვიყენეთ გარდაქმნა და age ცვლადი გარდავქმენით string ად


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)


num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
num4 = float(input("Enter number 4: "))
num5 = float(input("Enter number 5: "))

sum_numbers = num1 + num2 + num3 + num4 + num5
average = sum_numbers / 5

print("Average is:", average)



celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit is:", fahrenheit)



fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

print("Temperature in Celsius is:", celsius)