# 3.1
# operasi aritmatika 
a = 10
b = 3
#operasi tambahan +
hasil = a +b
print("a,'+',b,'=',hasil")
#operasi kurang -
hasil = a - b
print("a,'-',b,'=',hasil")
#operasi perkalian * 
hasil = a * b
print("a,'*',b,'=',hasil")
#operasi pembagian /
hasil = a / b
print("a,'/',b,'=',hasil")
#operasi eksponen (pangkat) **
hasil = a ** b
print("a,'**',b,'=,',hasil")
#operasi modulus %
hasil = a % b
print("a,'%',b,'=',hasil")
#operasi floor division //
hasil = a // b
print("a,'//',b,'=',hasil")

#3.2 
# latihan konversi satuan temperature 
#program konversi celcius ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATURE\n")
celcius = float (input ("masukan suhu dalam celcius :"))
print("suhu adalah", celcius ,"celcius")
#reamur
reamur = (4/5) * celcius 
print("suhu dalam reamur adalah ", reamur, "reamur")
#fahrenheit
fahrenheit = (9/5) * celcius + 32 
print("suhu dalam fahrenheit adalah ", fahrenheit, "fahrenheit")
#kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah ", kelvin, "kelvin")

#3.3
#operasi komperasi 
#setiap hasil dari operasi komperasi adalah boolean 
#>,<,>=,<=,==,!=,is,is not
a = 4
b = 2
# lebih besar dari >
print("=============== lebih besar dari (>)")
hasil = a > 3
print(a,'>',b,'=',hasil)
hasil = b > 3 
print(b,'>',b,'=',hasil)
hasil = b > 2
print(b,'>',b,'=',hasil)
#kurang dari <
print("=============== kurang dari (<)")
hasil = a < 3
print(a,'<',b,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print (b,'<',2,'=',hasil)
#lebih dari sama dengan >=
print("=============== lebih dari sama dengan (>=)")
hasil = a >= 3
print(a,'>=',b,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil =b >=2
print(b,'>=',2,'=',hasil)
#kurang dari sama dengan <=
print("=============== kurang dari sama dengan (<=)")
hasil = a <= 3
print(a,'<=',b,'=',hasil)
hasil =b <= 3
print(b,'<=',3,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)
#sama dengan ==
print("=============== sama dengan (==)")
hasil = a == 4
print(a,'==',b,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)
#tidak sama dengan !=
print("=============== tidak sama dengan (!=)")
hasil = a != 4 
print(a,'!=',b,'=',hasil)
hasil = b != 4
print(b,',=',4,'=',hasil)
#"is" sebagai komperasi obj identity (bukan literal)
x = 5 #ini adalah assignnment membuat object 
y = 5
hasil = x is y
print(x,'is',y, '=',hasil)
#'is not' sebagai komparasi obj identity (bukan literal)
x = 5 # ini adalah assignment membuat object
y =6
hasil = x is not y
print(x,'is not',y,'=',hasil)

#LATIHAN 
#input data dimensi bangunan
panjang = 12
lebar = 5 
tinggi = 8
#a.operasi aritmatika untuk menghitung luas, volume, dan keliling 
luas = panjang * lebar 
volume = panjang * lebar * tinggi 
keliling = 2 * (panjang + lebar) 
#b & c. operasi komparansi (perbandingan) 
apakah_luas_lebih_50 = luas > 50
apakah_volume_480 = volume == 480
#menampilkan hasil 
print("=== hasil perhitungan (aritmatika)===")
print(f"a. luas alas : {luas}")
print(f"   volume : {volume}")
print(f"   keliling : {keliling}")  
print("\n=== hasil pengecekan (komparansi)===")
print(f"b. Apakah luas > 50? : {apakah_luas_lebih_50}")
print(f"c. Apakah volume == 480 : {apakah_volume_480}")
print(f"c. Apakah volume == 480 : {apakah_volume_480}")