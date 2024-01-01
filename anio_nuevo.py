import time
import random

def fuegos_artificiales():
    for _ in range(25):
        print("\n" * random.randint(0, 5))
        for _ in range(random.randint(5, 15)):
            print("".join(random.choice([".", "o", "*", " "]) for _ in range(40)))
        time.sleep(0.5)
        print("\033[H\033[J")  # Esto borra la consola, válido para terminales UNIX

print("¡Feliz Año Nuevo 2024!\n")
fuegos_artificiales()