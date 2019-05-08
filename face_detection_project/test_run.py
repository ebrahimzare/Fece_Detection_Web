import cv2
import requests
url = "http://localhost:8000/face_detection/detect/"
##### image 1 #####
image_to_read = cv2.imread(r"D:\ebi\Python\virtualEnvs\DjangoEnv\Scripts\Face_Detection_Web"
                           r"\face_detection_project\image5.jpg")
tracker = {"url": "https://image.ibb.co/cPrdgS/image5.jpg"}
req = requests.post(url, data=tracker).json()
print("image3.png: {}".format(req))


for (w,x,y,z) in req["faces"]:
    cv2.rectangle(image_to_read,(w,x), (y,z), (0, 255, 0), 2)

cv2.imshow("image1.jpg", image_to_read)
cv2.waitKey(0)

#curl -X POST "http://localhost:8000/face_detection/detect/" -d "url=https://image.ibb.co/cPrdgS/image5.jpg";echo""