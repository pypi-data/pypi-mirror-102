import pymongo

class MongoData():
  def __init__(self, _host="mongodb01.51yomo.com", _port=27017, _user="cryptouser", _password="cryptouser", _dbName="cryptonews"):
    #self.mongoClient = pymongo.MongoClient("mongodb://cryptouser:cryptouser@127.0.0.1:27017/?authSource=cryptonews")
    self.mongoClient = pymongo.MongoClient(f"mongodb://{_user}:{_password}@{_host}:{_port}/?authSource={_dbName}")
    self.mongodb = self.mongoClient[_dbName]

  def appendData2Array(self, _collection,  _condition, _tag, _data):
    __collection = self.mongodb[_collection]
    if __collection.find(_condition).count() == 0:
        __collection.insert_one(_condition)
    __collection.update_one(_condition, {"$push": {_tag: _data}})

if __name__ == "__main__":
  __mongo = MongoData()
  __mongo.appendData2Array("BNBUTCD", {"date" : "20210221"}, "sma05", {"timestamp": 123456, "price": 1000}    )
  __mongo.appendData2Array("BNBUTCD", {"date" : "20210222"}, "sma05", {"timestamp": 123456, "price": 1000}    )

#{date: "20210221", sma05: [{timestamp: 1234567, price: 100}, {timestamp: 123458, price: 102}], sma10: [], sma20: [], boll20: [timestamp: 12345, data: [100, 105, 106]], boll40: 23456, data: [102, 103, 104], marketPrice: [{timestamp: 12345, price: 102}]}

