from time import sleep
import sys
import os

frase1 = 'Hola me llamo Juan'
frase2 = 'Hola me llamo Javi'
print(frase1, end='')
sys.stdout.flush()
sleep(1)
print(frase2)

# for i in range(100):
#     sys.stdout.write("\rProgress: {}%".format(i))
#     sys.stdout.flush()
#     time.sleep(0.1)
os.system('cls')