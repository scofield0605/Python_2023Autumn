# import pyrebase
from tkinter import *

config = {
    'apiKey': "AIzaSyCGg-is0rWvN-XwN3WpDDWpv7TQtEJUXng",
    'authDomain': "project-1166c.firebaseapp.com",
    'projectId': "project-1166c",
    'storageBucket': "project-1166c.appspot.com",
    'messagingSenderId': "740312905170",
    'appId': "1:740312905170:web:f0d5b96338beb18155c40b",
    'databaseURL':''
}
firebase=pyrebase.initialize_app(config)
auth=firebase.auth()

root = Tk()


loginlabel = Label(root, text = 'Login Page')
accountlabel = Label(root, text ='Account')
passwordlabel = Label(root, text ='Password')
resultLabel = Label(root, text = "")
#創建帳號和密碼愉入框
accountentry = Entry(root)
passwordentry = Entry(root, show="*")
#密飛喻入會顯示為星號
signUpbutton = Button(root, text ='Sign Up', width=10, command=lambda: addUser(root, accountentry, passwordentry))
loginbutton = Button(root, text = 'Log in', width=10, command=lambda: verifyUser (root, accountentry, passwordentry))
#放置元件
loginlabel.pack(pady=5)
accountlabel.pack(pady=5) 
accountentry.pack (pady=5)
passwordlabel.pack(pady=5) 
passwordentry.pack(pady=5)
signUpbutton.pack(pady=5)
#在標籤上方漆加間隔
resultLabel. pack (pady=5)
## sign up from Firebase function
def addUser(view, accountentry, passwordentry):
    print (accountentry.get(),passwordentry.get())
    print ("Signup...")
# Assign user's entry to parameter account and parameter password.
    account = accountentry.get()
    password = passwordentry.get()
    try:
        user = auth.create_user_with_email_and_password (account, password)
        print("Successfully signup!")
        resultLabel.config(text = "Successfully signup!") # reset label for successfully signup.
    except Exception as e:
# print("Email account has already exist!")
# resultLabel. config(text = "Email account has already exist!") # reset label for fail to signup.
        print (f"創建使用者失敗:{e}")# reset label for fail to signup.
        resultLabel["text"] = "Email account has already exist!"

def verifyUser(view, accountentry, passwordentry) :
    print(accountentry.get(),passwordentry.get())
    print("Log in...")
# Assign user's entry to parameter account and parameter password.
    account = accountentry.get()
    password = passwordentry.get()
    try:
        user = auth.sign_in_with_email_and_password(account, password)
        print("Successfully log in!")
        resultLabel.config(text = "Successfully log in!")
    except Exception as e:
        print (f"Logged in failed: {e}")
        resultLabel["text"] = "Logged in failed..."
root.mainloop()

# import firebase_admin
# from firebase_admin import credentials 
# from firebase_admin import firestore
# # import secret key
# # path/to/serviceAccount.json 請用自己存放的路徑
# cred = credentials.Certificate('/Users/scofield/Desktop/2023_autumn/Python_2023Autumn/firebase_token.json')
# # Initiate firebase
# firebase_admin.initialize_app(cred)
# # Initiate firestore
# db = firestore.client ()

