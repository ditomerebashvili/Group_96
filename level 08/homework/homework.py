#პითონში რამოდენიმე ტიპის შედარების ოპერატორი გვაქვს,ესენია:
# == უდრის
5 == 5   # True
3 == 4   # False

# !=  არ უდრის
5 != 3   # True
7 != 7   # False

# >  მეტია
10 > 5  # True
2 > 8   # False

# <  ნაკლებია
4 < 9   # True
10 < 7  # False

# >=  მეტია ან ტოლია(ერთ-ერთი მაინც უნდა შესრულდეს)
5 >= 5  # True
3 >= 7  # False

# <=  ნაკლებია ან ტოლია(ერთ ერთი მაინც უნდა შესრულდეს)
2 <= 5  # True
8 <= 3  # False



#ლოგიკური ოპერატორები
#გვაქვს ორი ტიპის ლოგიკური ოპერატორი and და or 
#and
#true and true - true (and მკაცრი ლოგიკური ოპერატორია და აუცილებლად ორივე პირობა უნდა შესრულდეს რათა true მივიღოთ,ანუ)
#true and false - false
#false and true - false
#false and false - false 

#or
#true or false - true
#false or true - true
#true or true - true
#false or false - false (თუ გვაქვს ერთი true მაინც,პასუხი იქნება true)
my_height = 175  # ჩემი სიმაღლე სანტიმეტრებში
user_height = int(input("შეიყვანეთ თქვენი სიმაღლე სანტიმეტრებში: "))

if user_height > my_height:
    print("თქვენ დიტოზე მაღალი ხართ.")
else:
    print("თქვენ დიტოზე დაბალი ხართ .")


    #num1 = "21"
#num2 = 21
#print(num1 == num2)  # False (გამოვა false რადგან string ტიპის და integer ტიპის მნიშვნელობების შედარება ვერ მოხდება  )

my_last_name = "Merebashvili"
user_last_name = input("შეიყვანეთ თქვენი გვარი: ")

if my_last_name == user_last_name:
    print("გვარები ემთხვევა.")
else:
    print("გვარები განსხვავდება.")


    #False or True and True and False გამოიტანს false ს 
    #True and False or False or True გამოიტანს true ს
    #True or True and False or True or False and True or False  გამოიტანს true ს



    temperature = float(input("შეიყვანეთ ოთახის ტემპერატურა გრადუსებში: "))

if temperature > 30:
    print("გაგრილება ჩართულია!")
else:
    print("გაგრილება არ არის საჭირო.")




    #HARD LEVEL
    # მომხმარებლისგან შემოსული ტემპერატურა გრადუსებში
celsius = float(input("შეიყვანეთ ოთახის ტემპერატურა გრადუსებში: "))

# გადაყვანა ფარენგეიტში
fahrenheit = celsius * 9 / 5 + 32

# პირობის შემოწმება
if fahrenheit > 89.6:
    print("გაგრილება ჩართულია! ტემპერატურა ფარენგეიტში:", fahrenheit)
else:
    print("გაგრილება არ არის საჭირო. ტემპერატურა ფარენგეიტში:", fahrenheit)
