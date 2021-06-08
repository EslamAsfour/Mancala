import pyrebase as pb

# preparations for multiplayer mode

firebaseConfig = {
    "apiKey": "AIzaSyA_SJF-bhXqdfst0Trux6CqOjIpXchKf88",
    "authDomain": "mancala-77b92.firebaseapp.com",
    "projectId": "mancala-77b92",
    "storageBucket": "mancala-77b92.appspot.com",
    "messagingSenderId": "456787053513",
    "appId": "1:456787053513:web:53cb366a2d99636bd27618",
    "measurementId": "G-7XHC9F34MV"
  }

firebase = pb.initialize_app(firebaseConfig)

realtime_db = firebase.database()
