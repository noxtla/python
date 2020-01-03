import os
import sys
import cv2
import numpy
import untite as mss
import pymysql
from tkinter import messagebox
from datetime import date
from datetime import datetime


now = datetime.now()
format = now.strftime('%d/%m/%Y \n%H: %M: %S')



conexion = pymysql.connect(host='remotemysql.com',
                        user='OuiwI9pjP2',
                        password='bKehdD6r9l',
                        db='OuiwI9pjP2')

dir_faces = 'udg/alumnos'


size = 4

(images, lables, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(dir_faces):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(dir_faces, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            lable = id
            images.append(cv2.imread(path, 0))
            lables.append(int(lable))
        id += 1
(im_width, im_height) = (112, 92)


(images, lables) = [numpy.array(lis) for lis in [images, lables]]
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, lables)


face_cascade = cv2.CascadeClassifier( 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    rval, frame = cap.read()
    frame=cv2.flip(frame,1,0)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #redimensionar la imagen
    mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))

    """buscamos las coordenadas de los rostros (si los hay) y
   guardamos su posicion"""
    faces = face_cascade.detectMultiScale(mini)
    
    for i in range(len(faces)):
        face_i = faces[i]
        (x, y, w, h) = [v * size for v in face_i]
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (im_width, im_height))

        # Intentado reconocer la cara
        prediction = model.predict(face_resize)
        
         #Dibujamos un rectangulo en las coordenadas del rostro
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cara = '%s' % (names [prediction[0]])
        
        #Si la prediccion tiene una exactitud menor a 100 se toma como prediccion valida
        if prediction[1]<100 :
          #Ponemos el nombre de la persona que se reconoció
          cv2.putText(frame,'%s - %.0f' % (cara,prediction[1]),(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))

          #En caso de que la cara sea de algun conocido se realizara determinadas accione          
          #Busca si los nombres de las personas reconocidas estan dentro de los que tienen acceso          
          #flabs.TuSiTuNo(cara)

        #Si la prediccion es mayor a 100 no es un reconomiento con la exactitud suficiente
        elif prediction[1]>101 and prediction[1]<500:           
            #Si la cara es desconocida, poner desconocido
            cv2.putText(frame, 'Desconocido',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))  

        #Mostramos la imagen
        cv2.imshow('OpenCV Reconocimiento facial', frame)

        if cara == "Desconocido":
            print("Eres desconocido pariente")
        else:
            
            cursor = conexion.cursor() 
            # En este caso no necesitamos limpiar ningún dato

            cursor.execute("SELECT id_chat FROM alumnos WHERE nombre = %s;", (cara,))

            # Con fetchall traemos todas las filas
            peliculas = cursor.fetchone()
            peliculas = int(peliculas[0])
            print(peliculas)
            mss.sms(peliculas)
            conexion.close()
            messagebox.showinfo("Bienvenido " + cara, "Asistencia registrada " + format)
            sys.exit("Asistencia registrada")
    #print(cara)

    #Si se presiona la tecla ESC se cierra el programa
