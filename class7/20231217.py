import firebase_admin
from firebase_admin import credentials 
from firebase_admin import firestore
# import secret key
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('/Users/scofield/Desktop/2023_autumn/Python_2023Autumn/firebase_token.json')
# Initiate firebase
firebase_admin.initialize_app(cred)
# Initiate firestore
db = firestore.client ()

doc = {'name':'Prince',
'email':'prince@gmail.com'
}
doc2 = {'name':'me',
'email':'ssss@gmail.com'
}



# doc_ref=db.collection("Autumn2023_Students").document("student01")
# doc_ref.set(doc)
# collection_ref = db.collection ("Autumn2023_Students")
# collection_ref.add(doc)

# doc1_ref=db.collection(" Autumn2023_Students ").document("student02")
# doc1_ref.set(doc2)

# path = "Autumn2023_Students/student01"
# doc_ref = db.document(path)
# path = "Autumn2023_Students"
# collection_ref = db.collection (path)
# docs = collection_ref.get()
# for doc in docs:
#     print("The content of document is:{}".format(doc.to_dict()))

# try:
#     doc = doc_ref.get()
#     doc_dict = doc.to_dict()
#     print("The content of the document is : ".format(doc_dict))
# except:
#     print ("The reference of document is not exist, please check the path is correct or not. {}".format(path))



# path = "Autumn2023_Students"
# collection_ref = db.collection(path)
# docs = collection_ref.where('name', '==','Prince').get()
# for doc in docs:
#     print("The content of document is: {}".format(doc.to_dict()))

# path = "Autumn2023_Students/student01"
# doc_ref = db.document(path)
# contacts = {
# 'email': 'prince@gmail.com',
# 'phone': '0910123456'
# }
# doc = {
# 'contacts': contacts
# }
# doc_ref.update(doc)

# path = "Autumn2023_Students/student01"
# doc_ref = db.document(path)
# doc = {
# 'contacts.email': 'abc@gmail.com'
# }
# doc_ref.update(doc)


path = "Autumn2023_Students/student02"
doc_ref = db.document(path)
doc_ref.delete()

students_ref = db.collection('Autumn2023_Students')
docs = students_ref.get()
for doc in docs:
    doc.reference.delete()
