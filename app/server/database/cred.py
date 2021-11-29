import os


# SECRET_KEY = os.environ.get('SECRET_KEY', input())
SECRET_KEY = os.environ.get('SECRET_KEY')


MONGO_DETAILS = "mongodb+srv://{}:{}@cluster0.jaby5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority".format("anaji_161121", SECRET_KEY)
