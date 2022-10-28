import pymongo
from pymongo import MongoClient
myclient= MongoClient("mongodb://localhost:27017/")
mydb=myclient['TD1']
collection=mydb['PhNoDir1']
#insert_One
#mydict = { "name": "Poonam", "PhoneNo":123, "address": "Highway 37","city":"Chennai" }

#x = collection.insert_one(mydict)
#insert_many
mylist1 = [ { "_id":1,"name": "Poonam", "PhoneNo":123, "address": "Highway 37","city":"Chennai" },
  { "_id":2,"name": "Mithraan","PhonNo":234,"address": "Apple st 652","city":"Munbai"},
  { "_id":3,"name": "Senthil","PhoneNo":456,"address": "Mountain 21","city":"Pune"},
  { "_id":4,"name": "Harshitha","PhoneNo":678, "address": "Valley 345","city":"Assam"},
  { "_id":5,"name": "Sandy","PhoneNo ":789 ,"address": "Ocean blvd 2","city":"Chennai"},
  { "_id":6,"name": "Uma","PhoneNo ":546 ,"address": "Green Grass 1", "city":"Bengaluru"},
  { "_id":7,"name": "Prem","PhoneNo ": 134 ,"address": "Sky st 331","city":"WestBengal"},
  {"_id":8,"name": "Abi","PhoneNo ":256,"address": "One way 98","city":"Chennai"},
  { "_id":9,"name": "Kayal","PhoneNo ":634 ,"address": "Yellow Garden 2","city":"Bengaluru"},
  { "_id":10,"name": "Saranya","PhoneNo ":579,"address": "Park Lane 38","city":"Bengaluru"},
  { "_id":11,"name": "Santhosh","PhoneNo ":853,"address": "Central st 954","city":"Chennai"},
  { "_id":12,"name": "Karthik","PhoneNo ":813,"address": "Main Road 989","city":"Mumbai"}
  
]
x1 = collection.insert_many(mylist1)

'''
#FindOne
x = collection.find_one()

print(x)

#findAll
for x in collection.find():
  print(x)
'''
#query1
'''
myquery = { "address": "Park Lane 38" }

mydoc = collection.find(myquery)

for x in mydoc:
  print(x)
  '''


#address greater than S:
'''
myquery1 = { "address": {"$gt": "S"} }

mydoc1 = collection.find(myquery1)

for x1 in mydoc1:
  print(x1)
  '''
#address starts with S:
'''
myquery3 = { "address": { "$regex": "^S" } }

mydoc2 = collection.find(myquery3)

for x2 in mydoc2:
  print(x2)
  '''
#Name in Alphabitical order
'''
mydoc3 = collection.find().sort("name")

for x3 in mydoc3:
  print(x3)
  '''
#UpdateOne
'''
myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

collection.update_one(myquery, newvalues)

#print "customers" after the update:
for x in collection.find():
  print(x)
  '''
#updatemany
'''
myquery1 = { "address": { "$regex": "^C" } }
newvalues1 = { "$set": { "name": "Hema" } }

x = collection.update_many(myquery1, newvalues1)

print(x.modified_count, "documents updated.")
'''
#DeleteOneOperation
'''
myquery = { "name": "Saranya" }

collection.delete_one(myquery)

#print the customers collection after the deletion:
for x in collection.find():
  print(x)
  '''
#DeleteManyOpertion
'''
myquery = { "city": {"$regex": "^M"} }

x = collection.delete_many(myquery)

print(x.deleted_count, "documents deleted")
'''
#DeleteAllDocuments
#x = collection.delete_many({})
#print(x)
#Drop
#collection.drop()



