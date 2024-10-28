palabra_nueva = input("Introduce una nueva palabra: ")
with open('palabras.txt', 'a') as archivo:
    archivo.write(palabra_nueva + '\n')
print("Palabra añadida exitosamente.")
