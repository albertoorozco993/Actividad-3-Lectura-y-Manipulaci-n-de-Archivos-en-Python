with open('palabras.txt', 'r') as archivo:
    palabras = [linea.strip() for linea in archivo.readlines()]
palabras_unicas = list(set(palabras))
with open('palabras_unicas.txt', 'w') as archivo_unicas:
    for palabra in palabras_unicas:
        archivo_unicas.write(palabra + '\n')
print("Archivo 'palabras_unicas.txt' creado sin duplicados.")
