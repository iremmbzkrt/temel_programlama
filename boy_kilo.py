print("Vücut Kitle İndeksi Hesaplama")
boy = float(input("Boyunuzu giriniz: "))
kilo = float(input("Kilonuzu giriniz: "))

endeks = kilo/(boy*boy)

if endeks <18:
    print("Zayıfsınız. VKİ: {}".format(endeks))
elif endeks >=18 and endeks < 25:
    print("Kilonuz normal. VKİ: {}".format(endeks))
elif endeks >=25 and endeks < 30:
    print("Kilolusunuz. VKİ: {}".format(endeks))
elif endeks >=30 and endeks <35:
    print("Obezite başlangıcı. VKİ: {}".format(endeks))
else:
    print("Ciddi obezite. VKİ: {}".format(endeks))
