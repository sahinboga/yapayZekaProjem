import cv2
import numpy as np
import os, json, math
import matplotlib.pyplot as plt


def AgeAndGender(ay):

    faceCascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

    MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
    age_data = [0,0,0,0,0,0,0,0]
    gender_data = [0, 0] #0. index kadin, 1. index erkek
    def load_caffe_models():
        age_net = cv2.dnn.readNetFromCaffe('data/deploy_age.prototxt', 'data/age_net.caffemodel')
        gender_net = cv2.dnn.readNetFromCaffe('data/deploy_gender.prototxt', 'data/gender_net.caffemodel')
        return age_net, gender_net

    path = "dataset/"+ay+"/"
    for i in os.listdir(path):

        image = cv2.imread(path+i)
        
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3)


        for(x,y,w,h) in faces:

             age_net, gender_net = load_caffe_models()
             face_img = image[y:y + h, h:h + w].copy()
             blob = cv2.dnn.blobFromImage(face_img, 1, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

             gender_net.setInput(blob)
             gender_preds = gender_net.forward()

             gender_data[gender_preds[0].argmax()] += 1


             age_net.setInput(blob)
             age_preds = age_net.forward()
             age_data[age_preds[0].argmax()] += 1
    return age_data, gender_data

f = open("data.json", "a")
data=[]
for i in range(12):
    age_data, gender_data = AgeAndGender(str(i+1))
    x = {
                "ay": i+1,
                "gender": gender_data,
                "age": age_data
                
            }
                
    data.append(x)
json.dump(data,f)
f.close()
   

    

