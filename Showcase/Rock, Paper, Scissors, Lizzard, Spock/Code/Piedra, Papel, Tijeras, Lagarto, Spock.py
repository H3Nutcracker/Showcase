import random

print("Juguemos a Piedra, Papel, Tijeras, Lagarto, Spock. El mejor de 7 gana:")
print("Escoge: \n1-Piedra 🪨 \n2-Papel 📃 \n3-Tijeras ✂️ \n4-Lagarto 🦎 \n5-Spock 🖖🏼 ")
print("En esta versión del juego clásico, se añaden dos nuevos elementos para hacerlo más complicado y menos probable a empatar.")
print("""En este juego las reglas son muy sencillas:
    Las Tijeras ✂️ cortan el Papel 📃
    El Papel 📃 cubre a la Piedra 🪨
    La Piedra 🪨 aplasta al Lagarto 🦎
    El Lagarto 🦎 envenena a Spock 🖖🏼
    Spock 🖖🏼 destroza las Tijeras ✂️
    Las Tijeras ✂️ decapitan al Lagarto 🦎
    El Lagarto 🦎 se come el Papel 📃
    El Papel 📃 niega a Spock 🖖🏼
    Spock 🖖🏼 vaporiza a la Piedra 🪨
    Y como siempre ha sido, la Piedra 🪨 aplasta las Tijeras ✂️
    """)

while True:
    cpu_score = 0
    user_score = 0

    while cpu_score < 5 and user_score < 5:
        cpu = random.randint(1, 5)

        if cpu == 1:
            cpu = "Piedra 🪨"
        elif cpu == 2:
            cpu = "Papel 📃"
        elif cpu == 3:
            cpu = "Tijeras ✂️"
        elif cpu == 4:
            cpu = "Lagarto 🦎"
        elif cpu == 5:
            cpu = "Spock 🖖🏼"

        try:
            user = int(input("Escoge un número para sacar Piedra, Papel, Tijeras, Lagarto o Spock: "))
            if user == 1:
                user = "Piedra 🪨"
                print("Escogiste Piedra 🪨")
            elif user == 2:
                user = "Papel 📃"
                print("Escogiste Papel 📃")
            elif user == 3:
                user = "Tijeras ✂️"
                print("Escogiste Tijeras ✂️")
            elif user == 4:
                user = "Lagarto 🦎"
                print("Escogiste Lagarto 🦎")
            elif user == 5:
                user = "Spock 🖖🏼"
                print("Escogiste Spock 🖖🏼")
            else:
                raise ValueError
        except ValueError:
            print(("ERROR TIENES QUE ESCOGER UN NUMERO ENTRE 1 & 5"))

        if cpu == user:
            print(f"La computadora sacó: {cpu}")
            print("Empate.")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif cpu == "Tijeras ✂️" and user == "Papel 📃":
            cpu_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Perdiste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif user == "Tijeras ✂️" and cpu == "Papel 📃":
            user_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Ganaste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif cpu == "Papel 📃" and user == "Piedra 🪨":
            cpu_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Perdiste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif user == "Papel 📃" and cpu == "Piedra 🪨":
            user_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Ganaste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif cpu == "Piedra 🪨" and user == "Lagarto 🦎":
            cpu_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Perdiste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif user == "Piedra 🪨" and cpu == "Lagarto 🦎":
            user_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Ganaste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif cpu == "Lagarto 🦎" and user == "Spock 🖖🏼":
            cpu_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Perdiste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif user == "Lagarto 🦎" and cpu == "Spock 🖖🏼":
            user_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Ganaste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif cpu == "Spock 🖖🏼" and user == "Tijeras ✂️":
            cpu_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Perdiste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif user == "Spock 🖖🏼" and cpu == "Tijeras ✂️":
            user_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Ganaste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif cpu == "Tijeras ✂️" and user == "Lagarto 🦎":
            cpu_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Perdiste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif user == "Tijeras ✂️" and cpu == "Lagarto 🦎":
            user_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Ganaste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif cpu == "Lagarto 🦎" and user == "Papel 📃":
            cpu_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Perdiste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif user == "Lagarto 🦎" and cpu == "Papel 📃":
            user_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Ganaste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif cpu == "Papel 📃" and user == "Spock 🖖🏼":
            cpu_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Perdiste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif user == "Papel 📃" and cpu == "Spock 🖖🏼":
            user_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Ganaste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif cpu == "Spock 🖖🏼" and user == "Piedra 🪨":
            cpu_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Perdiste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif user == "Spock 🖖🏼" and cpu == "Piedra 🪨":
            user_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Ganaste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif cpu == "Piedra 🪨" and user == "Tijeras ✂️":
            cpu_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Perdiste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        elif user == "Piedra 🪨" and cpu == "Tijeras ✂️":
            user_score += 1
            print(f"La computadora sacó: {cpu}")
            print("Ganaste")
            print(f"PUNTUACIÓN:\nTÚ: {user_score}\nCOMPUTADORA: {cpu_score}")

        if user_score == 5:
            print("Ganaste la partida")
        elif cpu_score == 5:
            print("La computadora ganó la partida")

    answer = input("¿Quieres jugar de nuevo? (s/n): ")

    if answer.lower() != "s":
        print("Gracias por jugar! Hasta la próxima")
        input("Pulsa enter o cierra la ventana para finalizar el programa")
        break