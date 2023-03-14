import cv2
import pyautogui

# Se genera una ventana con el nombre Mouse Pesition
cv2.namedWindow('MOuse PEsition')


# Definimos la función que va a mostrar las coordenadas del puntero

def show_MOuse_PEsition(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        # obtenesmos las coordenadas del puntero
        mouse_pesition=f'X:{x},Y:{y}'

        # otorgamos fondo a la venta
        img= cv2.rectangle (param,(0,0), (300,30),(0,0,0),-1)

        # escribe las coordenadas del puntero en la ventana
        img=cv2.putText(img, mouse_pesition, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255),1)

        # Muestra la imagen en la ventana
        cv2.imgshow('MOuse PEsition', cv2.zeros((20,300,3), dtype='uint8'))


        #Ciclo principal del programa

        while True:
            cv2.waitKey(1)
             # Si se presiona la tecla 'q', se ciera la ventana
            if cv2.waitKey(1)== ord('q'):
             break



# Cierra todas las ventanas
cv2.destroyAllWindows()


