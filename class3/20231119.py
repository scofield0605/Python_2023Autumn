#套用 pyrebase 套件,並連結firebaseproject 中的 app ,成功執行。
import pyrebase

# config = {
#     'apiKey': "AIzaSyCGg-is0rWvN-XwN3WpDDWpv7TQtEJUXng",
#     'authDomain': "project-1166c.firebaseapp.com",
#     'projectId': "project-1166c",
#     'storageBucket': "project-1166c.appspot.com",
#     'messagingSenderId': "740312905170",
#     'appId': "1:740312905170:web:f0d5b96338beb18155c40b",
#     'databaseURL':''
# }


#創建使用者帳戶。利用 pyrebase 套件中已經寫好的 function:create_user_with_email_and_password(email,password),即可快速建立 useraccount。

def signup():
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    user = auth.create_user_with_email_and_password(email, password)
    print("Successfully signup!")

#建立第一個節點。1. 建立物件。2. 將指標欄 (next)設定為None。

# Initiate the first element of single linked list.
head = Car('red')
head.next = None

# Connect firebase and the python script by using app config.
firebase = pyrebase.initialize_app(config)
# Get a reference to the auth service
auth = firebase.auth()