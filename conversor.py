def convertir(valor, desde, hacia):
    if desde == "C" and hacia == "F":
        return round((valor * 9/5) + 32, 2)
