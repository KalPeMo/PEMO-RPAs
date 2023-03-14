import pyautogui
import time
import tkinter as tk

#Definimos la posicion del objetivo
x,y=500,500

#Graduamos la velocidad en la que va hacerlo, en segundos
duration=2

#Obtener la posición actual del cursor del mouse
current_x, current_y=pyautogui.position()

#Calcular la distancia euclidiana entre la posicion actual y la posicion objetivo
distance=((x-current_x)**2+(y-current_y)**2)**0.5

#calcular la velocidad del movimiento en pixeles por segundo
speed=distance/duration

#mover el cursor del mouse hacia la posición objetivo
#pyautogui.moveTo(x,y, duration=duration, tween=pyautogui.easeInOutQuad)

#mover el cursor del mouse en tiempo real para evidenciar transparencia en el codigo
start_time=time.time()
while time.time() - start_time <= duration:
        #Calcular la nueva posición del cursor del mouse
        elapsed_time=time.time()-start_time
        progress=elapsed_time/duration
        tween_progress=pyautogui.easeInOutQuad(progress)
        new_x=int(current_x+(x-current_x)*tween_progress)
        new_y=int(current_y+(y-current_y)*tween_progress)

        #mover el cursor del mouse a la nueva posición
        pyautogui.moveTo(new_x,new_y)

        #Esperar un breve instante antes de actualizar la posición del cursor
        time.sleep(0.001)

