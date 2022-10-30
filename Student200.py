import pymongo
import json
from pymongo import MongoClient


# Making Connection
myclient = MongoClient("mongodb://localhost:27017/")
db = myclient["GuviGeek"]
collection = db["GeekNetwork"]


with open(r"C:/Users/Senthil/STUDENTS.json") as f:
    for file in f:
        myDict = json.loads(file)
        print(myDict)
        
#Total marks of Students       
'''
    

Tot_sum=collection.aggregate([{"$unwind":"$scores"}, {"$group":{
                               "_id":"$_id",
                               "Total":{"$sum":"$scores.score"}}
                               
                                }])
for i in Tot_sum:
    print(i)
    '''

#Average Marks of All Students
'''    
 
Agg_sum=collection.aggregate([{"$unwind":"$scores"}, {"$group":{
                               "_id":"$name",
                               "Average":{"$avg":"$scores.score"}}
                               
                                }])
for i in Agg_sum:
    print(i)

'''
#maximum marks of all Students
'''
max_score=collection.aggregate([{"$unwind":"$scores"}, {"$group":{
                               "_id":"$name",
                               "max_mark":{"$max":"$scores.score"}}
                               
                                }])
for i in max_score:
    print(i)
'''
#Sorting the marks in Decending order
'''      
sortavg=[]
Agg_sum=collection.aggregate([
    
{"$unwind":"$scores"}, {"$group":{
                               "_id":"$_id",
                               "Average":{"$avg":"$scores.score"}
                               }}, {"$sort":{"Average":-1}}
                               
                                 ]
                                   )
for i in Agg_sum:
    sortavg.append(i)
res=collection.bulk_write(sortavg)
myclient.close()
'''
'''
low_mark=collection.aggregate([{"$project":{"name":"$name","score":"$scores","Lowmark":{ "$lt": [ "$avg", 40 ]}}},
                                    {"$unwind":"$scores"}, {"$group":{
                                    "_id":"$name",
                                    "Average":{"$avg":"$scores.score"}}
                                                                                                                       }   

                               
                                 ]
                                   )
for i in low_mark:
    print(i)
    '''
'''
stdscore=db.collection.find({"scores" : { "$elemMatch":{"score":{"$gt" : 40 , "$lt" :100}}}});

for i in stdscore:
    print(i)
'''
'''
a1=db.collection.find({"scores" : {"$gte" : 40, "$lte" : 100}})

for i in a1:
    print(i)
 
   '''
'''   
a2=db.collection.find({})
for i in a2:
    print(i)
    '''
'''
db2=db.collection.aggregate([
   {
    "$group": {
      "_id": "$_id",
      "scores": {
        "$first": "$scores"
      },
      "data": {
        "$push": "$$ROOT"
      }
    }
  },
  {
    "$unwind": "$data"
  },
  {
    "$match": {
      "data.scores.type": "exam"
    }
  },
  {
    "$sort": {
      "data.scores.score": -1
    }
  },
  {
    "$project": {
      "_id": 1,
      "name": "$data.name",
      "scores": "$scores"
    }
  },
  {
    "$limit": 1
  }
])

for i in db2:
    print(i)
    '''