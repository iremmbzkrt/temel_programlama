vize = input("Vize notunuz: ")
final = input("Final notunuz: ")
ortalama = (float(vize)*0.4) + (float(final)*0.6)
print("Ortalama: {0}".format(ortalama))

if (ortalama < 45):
    print("Kaldınız")
else:
    print("Geçtiniz.")
