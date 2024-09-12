import math

def luas_lingkaran(r):
    return math.pi * r ** 2


r = float(input("Masukkan jari-jari lingkaran: "))

luas = luas_lingkaran(r)

print(f"Luas lingkaran dengan jari-jari {r} adalah {luas:.2f}")
