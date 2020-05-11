import os
import random
lista=[]
for root, dirs, files in os.walk("./Imagenes/Animales"):
    for filename in files:
        lista.append(filename)
print(random.choice(lista))