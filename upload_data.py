from pymongo.mongo_client import MongoClient
import pandas as pd
import json
uri = "mongodb+srv://madiharahman7may:Madiharahman7may@cluster0.qjhtira.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

df = pd.read_csv(r"D:\Desktop\MLproject\SensorFaultDetection\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)

json_record=json.loads(df.T.to_json)
# Create a new client and connect to the server
client = MongoClient(uri)

# create database name and collection name
DATABASE_NAME="MadihaRahman"
COLLECTION_NAME="waferfault"

#now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
