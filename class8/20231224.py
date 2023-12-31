import firebase_admin
from firebase_admin import credentials, storage
cred = credentials.Certificate("/Users/scofield/Desktop/2023_autumn/Python_2023Autumn/firebase_token.json")
firebase_admin.initialize_app(cred,{'storageBucket' : 'project-1166c.appspot.com'})
# connecting to firebase

file_path = "/Users/scofield/Desktop/2023_autumn/Python_2023Autumn/class8/Firebase_project/image/bed1.jpg"
bucket = storage.bucket() # storage bucket
blob = bucket.blob(file_path)
blob.upload_from_filename(file_path)