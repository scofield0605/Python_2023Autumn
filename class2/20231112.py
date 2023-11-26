import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
cred = credentials.Certificate("/Users/scofield/Desktop/python/Python_2023Autumn/firebase_token.json")
firebase_admin.initialize_app(cred)
email = "scofieldtsai@gmail.com"
password = "123456789"

user = auth.create_user(email=email, password=password)
print("User create successfully! {}",format(user.uid))

