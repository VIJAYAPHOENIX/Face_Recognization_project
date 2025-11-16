import os
import cv2 as cv
import numpy as np
from PIL import Image

recognizer = cv.face.LBPHFaceRecognizer_create()
path = "dataset"

def get_images_with_id(path):
    image_paths = [os.path.join(path,f) for f in os.listdir(path)]          # Set images path to os
    faces = []
    ids = []
    for single_image_path in image_paths:
        faceImage = Image.open(single_image_path).convert('L')
        faceNp = np.array(faceImage,np.uint8)
        id = int(os.path.split(single_image_path)[-1].split(".")[1])
        print(id)
        faces.append(faceNp)
        ids.append(id)
        cv.imshow("training",faceNp)
        cv.waitKey(10)
    return np.array(ids),faces

ids,faces = get_images_with_id(path)
recognizer.train(faces,ids)
recognizer.save('Recognizer/trained.yml')


cv.destroyAllWindows()











