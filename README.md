# Face_Recognization_project
<br>
It is a python based project and postgresql.<br>
To run the project first you have to install the following libraries.<br>
1." psycopg2 " to connect with postgresql.<br>
2." opencv-contrib-python " to help with face detection.<br>
3." Pillow " library.<br>
4. And make sure you download to "Haarcascade_frontalface_default.xml" file.<br>
5. And create two empty folders name as "Dataset" and "Recognizer".<br>
<br>
Here is the process to run the program step by step:<br>
1. Create a database in postgresql server and name it as "Face_recognization".<br>
2. Now run the "dataset_generator.py" to run the program .<br>
--> It asks about Id,Name,age --> and kindly enter the data as you wish.<br>
--> It captures the image of the face infront of the laptop camera.<br>
--> Caputured images are saved in the Dataset folder in ".jpg" format.<br>
4. Secondly, run the "training_dataset.py" to train the images.<br>
--> After training the images and saves results as "trained.yml" file.<br>
--> It saved in "Recognizer" folder.<br>
5. And finally run the "face_detection.py" to see the results.<br>
