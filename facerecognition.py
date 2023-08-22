import cv2
#first enable camera
face_capture=cv2.CascadeClassifier("C:/Users/khush/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0/LocalCache/local-packages/Python310/site-packages/cv2/data/haarcascade_frontalface_default.xml") 
#go to the address where cv2 was installed and then go to data and then you have pre-defined code for face recognition
#capture eyes,nose,ears,mouth
video_capture=cv2.VideoCapture(0)
while True :
    ret, video_data=video_capture.read()
    #to read images,video_cap will capture the videos
    #to show the images , we need frames which has title and a video running
    #to convert the images to black and white
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    #to cover and capture face data 
    faces=face_capture.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    #to create box
    for(x,y,w,h) in faces:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0.255,0),2)
        #rectangle makes square box
    cv2.imshow("video_live",video_data)
    #waitkey shows the images for a particular time period
    if cv2.waitKey(10) == ord("a"):    
        break
video_capture.release()
#video was enabled
#to capture face we need a variable




#first enable camera
#video_capture=cv2.VideoCapture(0)
#while True :
    #ret, video_data=video_capture.read()
    #to read images,video_cap will capture the videos
    #to show the images , we need frames which has title and a video running
    #cv2.imshow("video_live",video_data)
    #waitkey shows the images for a particular time period
    #if cv2.waitKey(10) == ord("a"):    
       # break
#video_capture.release()
#video was enabled