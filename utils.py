def konversi_suhu(nilai, dari, ke):
    dari = dari.lower()
    ke = ke.lower()


    if dari not in ["c", "f", "k", "r"] or ke not in ["c", "f", "k", "r"]:
        return "Error: Satuan tidak valid. Gunakan 'C', 'F', 'K', atau 'R'."


    if dari == "k" and nilai < 0:
        return "Error: Nilai Kelvin tidak boleh negatif."

  
    if dari == ke:
        return nilai

    if dari == "c":
        celsius = nilai
    elif dari == "f":
        celsius = (nilai - 32) * 5/9
    elif dari == "k":
        celsius = nilai - 273.15
    elif dari == "r":
        celsius = nilai * 5/4

    if ke == "c":
        return celsius
    elif ke == "f":
        return (celsius * 9/5) + 32
    elif ke == "k":
        return celsius + 273.15
    elif ke == "r":
        return celsius * 4/5