import firebase_admin
import pyrebase
import os
from firebase_admin import credentials, storage
cred = credentials.Certificate("/Users/scofield/Desktop/2023_autumn/Python_2023Autumn/firebase_token.json")
firebase_admin.initialize_app(cred,{'storageBucket' : 'project-1166c.appspot.com'})

config = {
    'apiKey': "AIzaSyCGg-is0rWvN-XwN3WpDDWpv7TQtEJUXng",
    'authDomain': "project-1166c.firebaseapp.com",
    'projectId': "project-1166c",
    'storageBucket': "project-1166c.appspot.com",
    'messagingSenderId': "740312905170",
    'appId': "1:740312905170:web:f0d5b96338beb18155c40b",
    'databaseURL':'',
    "serviceAccount":"/Users/scofield/Desktop/2023_autumn/Python_2023Autumn/firebase_token.json"
}

dir_path = "./Firebase_project 2/image"
filelist = [f for f in os.listdir(dir_path) if f.endswith(".jpg") or f.endswith(".png")]
print(filelist)



bucket = storage.bucket() # storage bucket
for file in filelist:
    file_path = dir_path+"/"+file
    blob_path = "project_images/"+file
    print("Now is uploading file {}.",format(file_path))
    blob = bucket.blob(blob_path)
    blob.upload_from_filename(file_path)

dir_name = "project_images"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)


# Connect firebase and the python script by using app config.
firebase = pyrebase.initialize_app(config)
# Get a reference to the auth service
storage = firebase.storage ()

all_files = storage.list_files ()
for file in all_files:
    if file.name.startswith(dir_name): # Only need the file starts with directory we want
        file.download_to_filename(file.name)

