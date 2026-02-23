age = int(input("enter your age:"))
height = int(input("enter your height:"))
print(age + height)
print(age * height)
print(age / height)
print(age % height)
print(bool(int(True) - int(False) + int(False))) #გამოიტანს True-ს რადგან შიგნითა ფრჩხილში ვიღებთ 1-0+0 რაც არის 1 და გარეთა ფრჩხილით 1ს ვაძლევთ boolის მნიშვნელობას რაც არის true. true=1 false=0

#data conversion  ფუნქციებია int()  float() str() bool() 
age = int(input(15))  #int() გარდაქმნის ცვლადს integerad 
age = float(input(15)) # გარდაქმნის float ად ანუ 15.0 ად
age = str(input(15))  #გარდაქმნის string ად
age = bool(input(15)) #გარდაქმნის bool ად