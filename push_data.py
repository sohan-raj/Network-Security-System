import os
import sys
import json
import dotenv
dotenv.load_dotenv()


MONGO_DB_URL = os.getenv("MONGO_DB_URL")

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def cv_to_json(self,file_path):
        try:
            data = pd.read_csv(file_path )
            data.reset_index(drop=True,inplace=True)
            records =  list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            self.mongo_client = pymongo.MongoClient(MONGODB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
            
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
        
if __name__ == "__main__":
    file_path = 'network_data\phisingData.csv'
    database = "SohanAI"
    collection = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.cv_to_json(file_path)
    no_of_records = networkobj.insert_data_mongodb(records,database,collection)
    print(no_of_records)
    
    
    