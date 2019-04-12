from PIL import Image
import face_recognition
import cv2

image = face_recognition.load_image_file("aa.jpg")

face_locations = face_recognition.face_locations(image)

image1 = image*1
image1[:, :, 0] = image[:, :, 2]
image1[:, :, 2] = image[:, :, 0]
for (A, B, C, D) in face_locations:
    cv2.rectangle(image1, (D, A), (B, C), (0, 255, 0), 2)
cv2.imshow('image', image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
