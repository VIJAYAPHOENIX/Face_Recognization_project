import cv2 as cv
import numpy as np
import psycopg2 as pgbase

faceDetect = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv.VideoCapture(0)

def insert_or_update(Id,Name,age):
    conn = pgbase.connect(
        host='localhost',
        database='face_recognization',
        user='postgres',
        password='vijay',
        port=5432
    )
    cursor = conn.cursor()

    cursor.execute("select * from students where Id ="+str(Id))
    result = cursor.fetchone()


    if result :
        cursor.execute("update students set Name= %s, age = %s where Id = %s",(Name,age,Id))
    else:
        cursor.execute("insert into students (Id, Name, age) values(%s,%s,%s)",(Id,Name,age))

    conn.commit()
    cursor.close()
    conn.close()

# User defined variables

Id = (input("Insert Id : "))
Name = input("Insert Name : ")
age = int(input("Insert Age : "))

insert_or_update(Id,Name,age)

# To detect the face in the web camera

sampleNum = 0                        # Assume that there is no samples in dataset
while True:
    ret, frame = cam.read()          # OPEN CAMERA
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)          # CONVERT THE IMAGE INTO BGRGRAY COLOR
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)    # SCALE OF FACES
    for (x, y, w, h) in faces:
        sampleNum = sampleNum + 1               # IF FACE IS DETECTED INCREMENT DONE
        cv.imwrite("dataset/user."+str(Id)+"." +str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255,  0), 2)
        cv.waitKey(100)               # DELAY TIME
    cv.imshow("Face", frame)           # SHOW FACES DETECTED IN THE WEB CAMERA
    cv.waitKey(1)
    if sampleNum > 20 :                # IF DATASET IS GREATER THAN 20 BREAK
        break

cam.release()
cv.destroyAllWindows()           # TO CLOSE THE OUTPUT WINDOW  # EXIT























