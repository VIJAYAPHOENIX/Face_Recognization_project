import cv2 as cv
import numpy as np
import os
import psycopg2 as pgbase

face_detect = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv.VideoCapture(0)

recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('Recognizer/trained.yml')

def getprofile(id):
    conn = pgbase.connect(
        host='localhost',
        database='face_recognization',
        user='postgres',
        password='vijay',
        port=5432
    )
    cursor = conn.cursor()
    cursor.execute("select * from students where Id = %s",(id,))
    profile = None
    for row in cursor:
        profile = row

    conn.close()
    return profile

while True:
    ret, frame = cam.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_detect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf = recognizer.predict(gray[y:y+h,x:x+w])
        profile = getprofile(id)
        print(profile)
        if profile != None:
            cv.putText(frame,"Name:" +str(profile[1]),(x,y+h+20),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,127),2)
            cv.putText(frame,"age:"+str(profile[2]),(x, y+h+45),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,127),2)

    cv.imshow("FACE",frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()



















