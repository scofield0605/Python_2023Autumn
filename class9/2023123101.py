import pyrebase
import os
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

# Connect firebase and the python script by using app config.
firebase = pyrebase.initialize_app(config)
# Get a reference to the auth service
auth = firebase.auth ()

dir_name = "nature"
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