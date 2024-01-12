import numpy as np

kotak = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1])
segitiga = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1])

bobot = np.random.rand(len(kotak), len(kotak))

batas_besar = 1.0
batas_kecil = 0.1

laju_pembelajaran = 0.1

for _ in range(1000):
    
    output_kotak = np.dot(bobot, kotak)
    bobot += laju_pembelajaran * np.outer(kotak, output_kotak)

    output_segitiga = np.dot(bobot, segitiga)
    bobot -= laju_pembelajaran * np.outer(segitiga, output_segitiga)

    bobot /= np.max(bobot)
    bobot = np.clip(bobot, batas_kecil, batas_besar)

uji_pola = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1])
output_uji = np.dot(bobot, uji_pola)

print("Hasil uji pada pola baru:", output_uji)
if np.array_equal(output_uji, np.dot(bobot, kotak)):
    print("Jaringan mengenali pola kotak.")
elif np.array_equal(output_uji, np.dot(bobot, segitiga)):
    print("Jaringan mengenali pola segitiga.")
else:
    print("Jaringan tidak dapat mengenali pola.")
