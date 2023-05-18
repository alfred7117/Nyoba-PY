import cv2
import label_image
size = 4

#File Xml yg ingin digunakan
classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
#gw Menggunakan WebCam / Camera di PC gw
webcam = cv2.VideoCapture(0)

while True:
    (rval, im) = webcam.read()
    im=cv2.flip(im,1,0)#Flip dibalik
    #buat ngegedein gambar
    mini = cv2.resize(im, (int(im.shape[1]/size), int(im.shape[0]/size)))
    #Buat ngedeteksi Muka / Yg lainnya
    faces = classifier.detectMultiScale(mini)
    #Draw Rectangles around each face
    for f in faces:
        (x, y, w, h) = [v * size for v in f] #ukurannya
        cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0), 4)
        #menyimpan Kotak di SubRecFaces
        sub_face= im[y:y+h, x:x+w]
        FaceFileName = "File.jpg" #Save the image as File.jpg
        cv2.imwrite(FaceFileName, sub_face)
        #Hasil foto lalu diclassification
        text = label_image.main(FaceFileName)
        text = text.title() #biar judulnya kek berhenti gt
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(im, text,(x+w,y), font, 1, (0,0,255), 2)
    #show image
    cv2.imshow('Capture',  im)
    key = cv2.waitKey(10)
    if key == 27:
        break


