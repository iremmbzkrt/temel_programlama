from random import randint

rand = randint(1, 100)
sayac = 0

while True:
    sayac += 1
    sayi = int(input("1 ile 100 arasında bir değer giriniz. 0'a basarsak çıkış."))
    if(sayi==0):
        print("Çıkış yaptınız.")
        break
    elif sayi < rand:
        print("Daha yüksek bir değer giriniz.")
        continue
    elif sayi > rand:
        print("Daha düşük bir değer giriniz.")
        continue
    else:
        print("Rastgele seçilen sayı {0}!".format(rand))
        print("Tahmin sayınız: {0}".format(sayac))
