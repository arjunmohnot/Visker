from google.cloud import storage
from firebase import firebase
import os
import urllib
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'visker-ede34-firebase-adminsdk-u8kfs-adeefaeb4f.json'
firebase=firebase.FirebaseApplication('https://visker-ede34.appspot.com/')
client=storage.Client()
bucket=client.get_bucket('visker-ede34.appspot.com')
blobs=bucket.list_blobs()
imageBlob=bucket.blob("images/1.jpg")
imageBlob.upload_from_filename('thor.jpg')
imageBlob=bucket.blob("images/2.jpg")
imageBlob.upload_from_filename('image.jpg')
storage = firebase.storage()
storage.child("images/example.jpg").download("img")