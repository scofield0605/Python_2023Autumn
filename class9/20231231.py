import firebase_admin
import os
from firebase_admin import credentials, storage
cred = credentials.Certificate("/Users/scofield/Desktop/2023_autumn/Python_2023Autumn/firebase_token.json")
firebase_admin.initialize_app(cred,{'storageBucket' : 'project-1166c.appspot.com'})

file_path = "/Users/scofield/Desktop/2023_autumn/Python_2023Autumn/class9/Sea Download.jpeg"
bucket = storage.bucket() # storage bucket
# blob = bucket.blob(file_path)
# blob.upload_from_filename(file_path)
# def upload_blob(bucket, source_file_name, destination_blob_name):
#     blob = bucket.blob(destination_blob_name)
#     blob.upload_from_filename(source_file_name)
#     print(f"File {source_file_name} uploaded to {destination_blob_name}.")
# upload_blob(bucket, '/Users/scofield/Desktop/2023_autumn/Python_2023Autumn/class9/Sea Download.jpeg', 'nature/beautifulsea.png')

dir_path = "./Taipei"
filelist = [f for f in os.listdir(dir_path) if f.endswith(".jpg")]
print(filelist)


# bucket = storage.bucket() # storage bucket
# for file in filelist:
#     file_path = dir_path+"/"+file
#     blob_path = "Taipei/"+file
#     print("Now is uploading file {}.",format(file_path))
#     blob = bucket.blob(blob_path)
#     blob.upload_from_filename(file_path)

bucket = storage.bucket ()
blob= bucket.blob("'nature/beautifulsea.png")
blob. download_to_filename('human_photo.png')



head = Car("red")
second = Car("blue")
head.next = second
second.next=head

def traverse(head) :
    ptr = head
    while True:
        print("The color of the car is {}.". format(ptr.color))
        ptr = ptr.next
        if ptr.next == None:
            break
    print("Finish traverse!")
traverse (head)