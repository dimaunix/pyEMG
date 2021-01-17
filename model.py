import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyAG8-KjfregQT81eoSscKaTGS2r8_xh8_I",
    "authDomain": "pyegm-5eb0f.firebaseapp.com",
    "databaseURL": "https://pyegm-5eb0f-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "pyegm-5eb0f",
    "storageBucket": "pyegm-5eb0f.appspot.com",
    "messagingSenderId": "593853163742",
    "appId": "1:593853163742:web:5593bd3dac9060ed107a4f"
}

firebase=pyrebase.initialize_app(firebaseConfig)

# db=firebase.database()
auth=firebase.auth()
# storage=firebase.storage()