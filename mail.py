from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#This script will not work in some restricted networks like bennett university.
#Use your own mobile data

try:
    img_data = open('some_image.png', 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'Keras Visualtion Tool Report'
    tempstring="The probability predicted by the "+datafr.label1+" model are"+str(datafr.d)
    text = MIMEText(tempstring)
    msg.attach(text)
    image_data = MIMEImage(img_data, name=os.path.basename('some_image.png'))
    msg.attach(image_data)
    img_data = open('assets/gradcam.jpg', 'rb').read()
    image_data = MIMEImage(img_data, name=os.path.basename('assets/gradcam.jpg'))
    msg.attach(image_data)
    img_data = open('assets/guided_backprop.jpg', 'rb').read()
    image_data = MIMEImage(img_data, name=os.path.basename('assets/guided_backprop.jpg'))
    msg.attach(image_data)
    img_data = open('assets/guided_gradcam.jpg', 'rb').read()
    image_data = MIMEImage(img_data, name=os.path.basename('assets/guided_gradcam.jpg'))
    msg.attach(image_data)
    FROM = "yourmail@gmail.com"
    TO = str(email).split(",") #to email

    import smtplib
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
    except:
         server = smtplib.SMTP('smtp.gmail.com', 465)
    server.starttls()
    server.login("yourmail@gmail.com", "yourpassword")
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
except Exception as e:
    print('mail error'+str(e))
