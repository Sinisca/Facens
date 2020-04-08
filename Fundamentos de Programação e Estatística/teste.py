import random

for x in range(12):
     print(random.randint(0, 50))


     def lista_random():
         lista = random.sample(range(0, 50), 12)
         lista.sort()
         return lista