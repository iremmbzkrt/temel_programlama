def ucgen():
    yukseklik = 5
    for i in range(1, yukseklik):
        print(" "*(yukseklik - i), "*"*(i*2-1))

ucgen()
