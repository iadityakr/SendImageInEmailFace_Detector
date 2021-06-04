import cv2
import smtplib, ssl
import smtplib, ssl
import imghdr
from email.message import EmailMessage
import time

model = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def sendMail():
    sender_email = "<Senders_Email>"
    reciever_email = "<Receivers_Email>"
    newMessage = EmailMessage()


    port = 465  # For SSL
    email = "<your_Email>"
    password = "<Your_Password>"

    newMessage['Subject'] = "Look what I found !!" 
    newMessage['From'] = sender_email                  
    newMessage['To'] = reciever_email 

    newMessage.set_content("Found a face, Have a Look ...")

    # Create a secure SSL context
    context = ssl.create_default_context()
    with open('face_found.jpg', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name

    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(email, password)
        server.send_message(newMessage)
    return


cap = cv2.VideoCapture(0)

while True:
    
    ret , photo = cap.read()
    faces = model.detectMultiScale(photo)
    
    if len(faces) == 0:
        pass
#     elif int(format(len(faces))) > 1:
#         time.sleep(3)
#         cv2.imwrite("face_found.jpg" , photo)
#         sendMail()
#         break
    elif int(format(len(faces))) > 0:
        x1 = faces[0][0]
        y1 = faces[0][1]
        x2 = x1+faces[0][2]
        y2 = y1+faces[0][3]
        
        rphoto = cv2.rectangle(photo , (x1,y1) , (x2,y2), [0,255,0] , 5)
        cv2.imshow('Adi' , rphoto)
        if cv2.waitKey(10) == 13:
            break
cv2.destroyAllWindows()
cap.release()
