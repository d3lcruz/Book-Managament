from pymongo.mongo_client import MongoClient
#from pymongo.server_api import ServerApi
uri = "mongodb+srv://Delacruz:machera@practica.26jbxza.mongodb.net/?retryWrites=true&w=majority&appName=Practica"
# Create a new client and connect to the server
client = MongoClient(uri)
db = client.Book_Managament
collection = db["books"]
users_collection = db["users"] 
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)