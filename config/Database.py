from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

class Database:
  
    def __init__(self):

        self.db=''

    def document_to_json(self, doc):

        doc["_id"] = str(doc["_id"])  # Convert ObjectId to string for JSON serialization
        return doc

    def connect(self):
        # Replace with your MongoDB connection string
        connection_string = "mongodb+srv://firstmongo:zgen5fAxj2d2TLLh@cluster0.qiiccaa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

        # Connect to MongoDB Atlas
        try:
            client = MongoClient(connection_string)
            # Access a specific database
            self.db = client["marsights"]

            print("Connection successful!")
        
        except ConnectionFailure:
            print("Failed to connect to MongoDB server.")
        except OperationFailure:
            print("Authentication failed.")
        except Exception as e:
            print("An error occurred:", e)

    def create_collection(self, collection_name, data):
        
        self.connect()

        result = self.db[collection_name].insert_one(data)

        #return result



    def get_all_record(self, collection_name):

        self.connect()

        articles = self.db[collection_name].find()

        #articles = self.document_to_json(articles)

        return list(map(self.document_to_json, articles))



