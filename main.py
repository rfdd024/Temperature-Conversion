from utils import konversi_suhu

print("=== KONVERSI SUHU ===")
print("Satuan: C (Celsius), F (Fahrenheit), K (Kelvin), R (Reamur)")

try:
    nilai = float(input("Masukkan nilai suhu: "))
    dari = input("Dari satuan (C/F/K/R): ").strip().lower()
    ke = input("Ke satuan (C/F/K/R): ").strip().lower()

    hasil = konversi_suhu(nilai, dari, ke)

    if isinstance(hasil, str): 
        print(hasil)
    else:
        satuan_map = {"c": "°C", "f": "°F", "k": "K", "r": "°R"}
        print(f"Hasil: {nilai}{satuan_map[dari]} = {hasil:.2f}{satuan_map[ke]}")

except ValueError:
    print("Error: Masukkan angka yang valid untuk suhu.")