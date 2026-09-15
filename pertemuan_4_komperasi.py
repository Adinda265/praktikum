 #4.1 LOGICAL
print("n/OPERASI LOGIKA ATAU BOOLEAN/n")
 #NOT
print("===NOT===")
a = True
c = not a
print('data a =',a)
print('=== NOT')
print('data c =',c)

 #OR (jika salah satu true hasilnya true)
print("===OR===")
mangga = False
jambu = False
jus = mangga or jambu
print("mangga ,'or', jambu ,'=', jus")
mangga = True
jambu = False
jus = mangga or jambu 
print("mangga ,'or', jambu ,'=', jus")
mangga = True
jambu = True 
jus = mangga or jambu 
print("mangga ,'or', jambu ,'=', jus") 

#AND (keduanya true hasilnya true)
print("===AND===") 
saya = False
anda = False
AK = saya and anda 
print("saya ,'and', anda ,'=', AK")
saya = False
anda = True
AK = saya and anda 
print("saya ,'and', anda,'=', AK")
saya = True 
anda = False
AK = saya and anda
print("saya ,'and', anda ,'=', AK")
saya = True
anda = True 
AK = saya and anda 
print("saya ,'and', anda ,'=', AK")

#XOR (akan true jika salah satu true, sisanya flase)
print("===XOR===")
hijau = False 
biru = False 
jadi = hijau ^ biru
print("hijau ,'xor', biru ,'=', jadi")
hijau = False 
biru = True 
jadi = hijau ^ biru 
print("hijau ,'xor', biru ,'=', jadi")
hijau = True 
biru = False 
jadi = hijau ^ biru
print("hijau ,'xor', biru ,'=', jadi")
hijau = True
biru = True
jadi = hijau ^ biru 
print("hijau ,'xor', biru ,'=', jadi")


#4.2 LOGIKA DAN KOMPARASI
print("n/LOGIKA DAN KOMPARASI/n")

#+++++5-----15+++++
angka = int(input("masukan angka\nkurang dari 5\natau\nlebih besar dari 15\n: "))
#kurang dari 5
kurang = (angka <5)
print("kurang dari 5 =",kurang)
#lebih dari 15 
lebih = (angka >15)
print("lebih dari 15 =",lebih)
correct = kurang or lebih
print("angka yang anda masukan: ",correct)

#-----5+++++15-----
#kasus irisan
angka = int(input("masukan angka \nlebih dari 5\dan\nkurang dari 15\n: "))
#lebih dari 5
lebih = (angka >5)
print("lebih dari 5 =",lebih)
#kurang dari 15
kurang = (angka <15)
print("kurang dari 15 =",kurang)
correct = lebih or kurang 
print("angka yang anda masukan: ",correct)


#4.3 IF AND ELSE
print("n/IF AND ELSE/n")
nama1 = input("siapa nama anda? ")

# 1. if inline 
if nama1=="bunga" :
     print("pintar")
else:
   print("km tidak pintar")
print("end program")

#4.4 ELIF STATEMENT 
nama2 = input("siapa nama anda? ")

# if kondisi:
#    asik true 
#elif kondisi:
#    asik true 
#elif kondisi 
#    asik true 
#else:
#    aksi

if nama2=="dinda": #kondisi 1
   print("hai dinda baik!!") #aksi true 1
elif nama2=="lina": #kondisi 2
   print("hai lina cantik!!") #aksi true 2
elif nama2=="lili": #kondisi 3
   print("hai lili pintar!!") #aksi true 3
else:
   print("au ah ga kenal!!!") #aksi flase
print("end program")