import random

element = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

panjang_pasword = int(input("Masukan panjang kata sandi:"))

password = ""
for i in range(panjang_pasword): 
    password += random.choice(element)

print(password)