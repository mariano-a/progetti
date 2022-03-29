import PySimpleGUI as sg
import cv2

#Carico il classificatore
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')

def stampaFinestra(m,t):
    sg.theme(t)
    layout = [[sg.Text(m)],
              [sg.Button("OK")]]
    # Creo la finestra
    window = sg.Window(' MESSAGGIO ', layout)
    # Creo un loop per mantenere la finestra aperta
    while True:
        event, values = window.read()
        # Se premo il bottone OK esco
        if event == "OK" or event == sg.WIN_CLOSED:
            break
    window.close()

#Legge un immagine e la converte in un oggetto OpenCV
img = cv2.imread('mascherinaCorretta.png')

# Affinchè il classificatore funzioni, converto il fotogramma in scala di grigi.
scala_grigi = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#Il metodo detectMultiScale () dell'oggetto face_cascade,
# riceve un frame(immagine) come argomento e fa scorrere il classificatore a cascata sull'immagine.
#face contiene tutti i rilevamenti dei volti
face = face_cascade.detectMultiScale(scala_grigi, 1.3, 5)

#per ogni faccia disegno un rettangolo con coordinate ai vertici a,b (alto sx) a+c,b+d(basso dx)
for(a,b,c,d) in face:
    img = cv2.rectangle(img, (a,b), (a+c,b+d), (255,0,0),2)
    ROI_grigi = scala_grigi[b:b+d, a:a+c]
    ROI_colore = img[b:b+d, a:a+c]

    mouth = mouth_cascade.detectMultiScale(ROI_grigi)
    #print('mouth: ', mouth)

    nose = nose_cascade.detectMultiScale(ROI_grigi)
    #print('nose: ', nose)

    if mouth == ():         #se NON rileva la bocca
        var1=False
    else:
        var1=True

    if nose == ():
        var2=False
    else:
        var2=True

    #print('var1: ', var1)
    #print('var2: ', var2)

    if var1==True:

              for(ex,ey,ew,eh) in mouth:
                  cv2.rectangle(ROI_colore,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                  cv2.imshow('img', img)
                  msg="MASCHERINA NON INDOSSATA"
                  tema='Darkred'
                  stampaFinestra(msg,tema)
    else:
                  if var2 == True:

                     for (nx, ny, nw, nh) in nose:
                       cv2.rectangle(ROI_colore, (nx, ny), (nx + nw, ny + nh), (0, 255, 0), 3)
                       cv2.imshow('img', img)
                       msg="MASCHERINA INDOSSATA PARZIALMENTE, COPRIRE ANCHE IL NASO"
                       tema='Darkred'
                       stampaFinestra(msg,tema)
                  else:
                       cv2.imshow('img', img)
                       msg="MASCHERINA INDOSSATA CORRETTAMENTE"
                       tema='Darkgreen'
                       stampaFinestra(msg,tema)


cv2.waitKey(0)
cv2.destroyAllWindows()
