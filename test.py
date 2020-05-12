import random

ruta = "./Text/frases.txt"
frases = []
with open(ruta) as my_file:
    for line in my_file:
        frases.append(line)
print(random.choice(frases))






'''import os
import random
lista=[]
for root, dirs, files in os.walk("./Imagenes/Animales"):
    for filename in files:
        lista.append(filename)
print(random.choice(lista))'''