
#print("\nTUGAS PERTEMUAN 5 'PENGULANGAN DAN KONTROL ALUR'\n") 

#print("========================")
#print("\nNOMER 1\n")
# tugas 1
angka1 = 1
while angka1 <=50:
    if angka1 % 2 == 0:
        print(f"{angka1} itu genap")
    else:
        print(f"{angka1} itu ganjil")
    angka1 += 1



# tugas 2
print("=========================")
print("\nNOMER 2\n")
angka2 = 2
while angka2 <= 100:
    pembagi = 2
    prima = True 
    while pembagi < angka2:
        if angka2 % pembagi == 0:
           prima = False 
           break
        pembagi += 1
    if prima:
        print(angka2, end=" ")
    angka2 += 1

print("\n=========\n")
for p in range (1,101):
    pembagi = 2
    prima = True 
    while pembagi < p:
        if p % pembagi == 0:
            prima = False
            break
        pembagi += 1
    if prima:
        print(f"{p}", end=" ")
    p += 1