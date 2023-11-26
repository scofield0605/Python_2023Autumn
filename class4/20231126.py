# import pyrebase

# config = {
#     'apiKey': "AIzaSyCGg-is0rWvN-XwN3WpDDWpv7TQtEJUXng",
#     'authDomain': "project-1166c.firebaseapp.com",
#     'projectId': "project-1166c",
#     'storageBucket': "project-1166c.appspot.com",
#     'messagingSenderId': "740312905170",
#     'appId': "1:740312905170:web:f0d5b96338beb18155c40b",
#     'databaseURL':''
# }

# firebase=pyrebase.initialize_app(config)
# auth=firebase.auth()

# def signup():
#     email = input("Please enter your email: ")
#     password = input ("Please enter your password: ")
#     try:
#         user = auth.create_user_with_email_and_password(email, password)
#         print("Successfully signup!")
#     except:
#         print('invaid email or password')

# def login():
#     print("Log in...")
#     email = input("Please enter your email: ")
#     password = input("Please enter your password: ")
#     try:
#         login=auth.sign_in_with_email_and_password(email, password)
#         print(login)
#         print("Successfully logged in!")
#     except:
#         print("Invalid email or password!")

# login()
# #signup()

# class car:
#     def _init_(self,color):
#         self.color= color
#         self.next=None
    
# head=car('red')
# head.next=None

def traverse(head):
    ptr = head
    while ptr != None:
        print('The color of the car is {}.'.format(ptr.color))
        ptr = ptr.next
print('Finish traverse!')