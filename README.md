# Face_Recognization_project
It is a python based project and postgresql.
To run the project first you have to install the following libraries.
1." psycopg2 " to connect with postgresql.
2." opencv-contrib-python " to help with face detection.
3." Pillow " library.
4. And make sure you download to "Haarcascade_frontalface_default.xml" file.
5. And create two empty folders name as "Dataset" and "Recognizer".

Here is the process to run the program step by step:
1. Create a database in postgresql server and name it as "Face_recognization".
2. Now run the "dataset_generator.py" to run the program .
--> It asks about Id,Name,age --> and kindly enter the data as you wish.
--> It captures the image of the face infront of the laptop camera.
--> Caputured images are saved in the Dataset folder in ".jpg" format.
4. Secondly, run the "training_dataset.py" to train the images.
--> After training the images and saves results as "trained.yml" file.
--> It saved in "Recognizer" folder.
5. And finally run the "face_detection.py" to see the results
