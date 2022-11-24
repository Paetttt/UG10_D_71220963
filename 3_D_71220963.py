t = int(input("Masukkan tahun: "))

if t % 400 == 0:
    print("{} merupakan tahun kabisat".format(t))
elif t % 100 == 0:
    print("{} bukan tahun kabisat".format(t))
elif t % 4 == 0:
    print("{} merupakan tahun kabisat".format(t))
else:
    print("{} bukan tahun kabisat".format(t))