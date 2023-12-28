import cv2
import numpy as np
from tensorflow.keras.models import model_from_json
import os

#Loading the classifier model
#Load the JSON file
json_file = open('model.json', 'r')
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)

#Load the model weights
model.load_weights('model.h5')

#Expression dictionary
expression_dict = {0:'Angry', 
           1:'Fear', 
           2:'Happy', 
           3:'Sad', 
           4:'Surprise', 
           5:'Neutral'
          }

font = cv2.FONT_HERSHEY_SIMPLEX

# Get user supplied values
#imagePath = "abba.png"
imagePath = "picture.png"
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    #cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w] 
    roi_color = image[y:y+h, x:x+w]
            
    #Crop each of the faces, resize, and use the classifier to classify the facial expression
    cropped_image = gray[y:y+h,x:x+w]
    cropped_image = cv2.resize(cropped_image, dsize=(48,48))
    reshaped = np.reshape(cropped_image, (1, 48,48,1))
    reshaped = np.divide(reshaped, 255.0)
    
    #Make a prediction
    expression = np.argmax(model.predict(reshaped))
    cv2.putText(image,expression_dict[expression],(x+10,y-10), font, 1,(100,100,100),3,cv2.LINE_AA)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
os.system("clear")
