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

loginlabel= Label(root, text= 'Login Page')
accountlabel = Label(root, text # 'Account')
passwordlabel= Label(root,text = 'Password')
resultlabel= Label(root, text .:)
#根號密碼输入程與註冊按钮
accountentry Entry(root)
passwordentry = Entry(root,show="*)#密碼輸入為*
signupbutton = Button(root,text ='Sign Up',width=10,command=lambda: addUser())
loginlabel. pack(pady=5)
account label. pack(pady=5)
password label. pack(pady=5)
resultlabeL. pack(pady=5)
accountentry-pack(pady=5)
passwordentry. pack(pady=5)
signupbutton.pack(pady=5)
def addUser(view,account)：
    accountentry = Entry(root)
    passwordentry= Entry(root,show="*")#密碼输入為*
    signupbutton = Button(root,text = 'Sign Up',width =10,command=lambda: addUser(root,accountentry,passwordentry))
#放置元素
Loginlabel.pack(pady=5)
account labe l. pack(pady=5)
passwordlabel.pack(pady=5)
resultlabel. pack(pady=5)
accountentry, pack(pady=5)
passwordentry.pack(pady=5)
signupbutton.pack(pady=5)

def addUser(giew, accountentry, passwordentry):
    print(accountentry.get(),passwordentry.get())
    print("Sign Up...")
#取得咕就密研並存成参教
account # accountentry.get()
password = passwordentry.get()
    try:
        auth.create_user_with_email_and_password(account,password)
      print("Successfully signup!")
    resultlabel.config(text"Successfully signup!")
except Exception as e:
print(f"Create Account Failed...: (e)")
resultlabel["text"] = "Create Account Failed..."



