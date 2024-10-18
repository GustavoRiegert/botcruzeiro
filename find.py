import pyautogui
import time

try:
    while True:
        # Obtém a posição atual do mouse
        x, y = pyautogui.position()
        print(f"Posição do mouse: X={x}, Y={y}")

        # Pausa por 1 segundo
        time.sleep(1)
except KeyboardInterrupt:
    print("Captura de posição interrompida.")
