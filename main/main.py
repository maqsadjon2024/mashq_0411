# 1-misol
sonlar = [-3, -1, 0, 2, 4, 5, -6]
musbat_kv = [x**2 for x in sonlar if x > 0]
print(musbat_kv)


# 2-misol
uchga_bolinadigan = [x for x in range(1, 51) if x % 3 == 0]
print(uchga_bolinadigan)


# 3-misol
satr = input("Satr kiriting: ")
katta_harfli = [harf.upper() for harf in satr]
print(katta_harfli)


# 4-misol
sonlar = [1, 3, 6, 8, 2, 10]
katta_5 = [x for x in sonlar if x > 5]
print(katta_5)


# 5-misol
tub_sonlar = [x for x in range(2, 101) if all(x % i != 0 for i in range(2, int(x**0.5)+1))]
print(tub_sonlar)


# 6-misol
satr = input("Matn kiriting: ")
unlilar = [harf for harf in satr if harf.lower() in 'aeiou']
print(unlilar)


# 7-misol
sonlar = [2, 4, 6, 8]
natija = [indeks * qiymat for indeks, qiymat in enumerate(sonlar)]
print(natija)


# 8-misol
sonlar = list(map(int, input("Sonlarni kiriting (bo‘sh joy bilan): ").split()))
juft_ikki = [x * 2 for x in sonlar if x % 2 == 0]
print(juft_ikki)


# 9-misol
satrlar = ["salom", "python", "hi", "dasturlash", "ok"]
uzun_satrlar = [s for s in satrlar if len(s) > 5]
print(uzun_satrlar)


# 10-misol
toq_kv = [x**2 for x in range(1, 21) if x % 2 != 0]
print(toq_kv)
