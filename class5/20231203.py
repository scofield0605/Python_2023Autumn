#引入 pyrebase 套件,並連結 firebaseproject。

# import pyrebase
# config = {
# "apiKey": "AIzaSyAjMxxIU0NmcQpSK_2uHCinqLBgxjXa4PY",
# "authDomain": "fir-test-49290.firebaseapp.com",
# "projectId": "fir-test-49290",
# "storageBucket": "fir-test-49290.appspot.com",
# "messagingSenderId": "1063305586124",
# "appId": "1:1063305586124:web:5d004c0233936c0a4de969”,
# "databaseURL": ""
# }
# # Connect firebase and the python script by using app config.
# firebase = pyrebase.initialize_app(config)
# # Get a reference to the auth service
# auth = firebase.auth()


# #當點下 Signupbutton會呼叫 addUser function。

# ## sign up from Firebase function
# def addUser(view, accountentry, passwordentry):
#     print(accountentry.get(),passwordentry.get())
#     print("Signup...")
# # Assign user's entry to parameter account and parameter password.
#     account = accountentry.get()
#     password = passwordentry.get()
#     try:
#         user = auth.create_user_with_email_and_password(account, password)
#         print("Successfully signup!")
#         resultLabel.config(text = "Successfully signup!") # reset label for successfully signup.
#     except Exception as e:
# # 發生錯誤時的處理
#         print(f"創建使用者失敗: {e}") # reset label for fail to signup.
#         resultLabel["text"] = "Invalid Email or Password!"
#         signUpbutton = Button(root, text = 'Sign Up', width=10, command=lambda: addUser(root, accountentry, passwordentry))


# #新節點插入第一個節點之前,成為單向串列的首節點。
# #將新節點 new 的指標指向原串列首節點。
# #將串列首指向新節點。

# new = Car("black") #Add the new element.
# new.next = head #The new first element points to the original head element.
# #Find the element(ptr) which points to the original head element and turns to point to new element.
# ptr = head
# while ptr.next != head:
# ptr = ptr.next
# ptr.next = new
# head = new #Set new head element.

# #刪除環狀串列的中間節點。
# #找到欲刪除的節點 delete 之前一個節點 previous。
# #將 previous 節點指向 delete 的下一個節點。
# # Find the element before the node you want to delete.
# ptr = head
# while ptr.next != delete:
#     ptr = ptr.next
# # Connect previous node of delete node to next node of delete node.
# ptr.next = ptr.next.next


import pyrebase
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