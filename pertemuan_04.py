#TUGAS 4
#input usia user 
usia = int(input("masukan usia anda: "))
#mengkategorikan berdasarkan usia 
if usia <=12 :
    print("anak-anak")
if usia >12 and usia <=17:
    print("remaja")
if usia >17 and usia <=59:
    print("dewasa")
if usia >59:
    print("lansia")