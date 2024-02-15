import cv2 

path_to_image = "" # enter the path to the image here
img = cv2.imread(path_to_image) 

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
face_cascade = cv2.CascadeClassifier('D:/SpecsDetection/haarcascade_frontalface_alt2.xml') # give the path to the haarcascade_frontalface_alt2.xml where you've save it on your computer
  
faces = face_cascade.detectMultiScale(gray, 1.1, 4) 

for (x, y, w, h) in faces: 
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2) 
    faces = img[y:y + h, x:x + w] 
    cv2.imshow("face",faces) 
    cv2.imwrite('face.jpg', faces) 
      
cv2.imwrite('detcted.jpg', img) 
cv2.imshow('img', img) 
cv2.waitKey()