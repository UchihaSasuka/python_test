import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

# db = client.test
# collection = db.students

# students = {
#     "id": "20190306",
#     "name": "Jordan",
#     "age": 20,
#     "gender": 'male'
# }

# student1 = {
#     "id": "20190306",
#     "name": "Mike",
#     "age": 20,
#     "gender": 'male'
# }
# student2 = {
#     "id": "20190306",
#     "name": "Bob",
#     "age": 22,
#     "gender": 'male'
# }
# result = collection.insert_many([student1, student2])
# print(result)
# print(result.inserted_ids)
#result = collection.find_one({'name':'Mike'})
#results = collection.find({'age':20})
#results = collection.find({'age': {'$gt': 20}})
#results = collection.find({'age': {'$in':[20,22]}})
# for result in results:
#     print(result)
# count = collection.count_documents({'age': 20})
# print(count)
#results = collection.find().sort('name', pymongo.ASCENDING).skip(1).limit(1)
# print([result['name'] for result in results])
#print([result['name'] for result in results])

# condition = {'name': 'Mike'}
# student = collection.find_one(condition)
# student['name'] = 'Fork'
# result = collection.update(condition, student)
# print(result)
#results = collection.update(condition, {'$set': student})
# student['age'] = 22
# result = collection.update_one(condition, {'$set': student})
# result = collection.update_many(condition, {'$inc': {'age', 1}})
# print(result)

# result = collection.delete_one({'name':'Kevin', 'age':10})
# result = condition.delete_many({'age':{'$gt': 25}})
# print(result)
# print(result.deleted_count)
db = client.weibo
collection = db.weibo

results = collection.find()
for result in results:
    print(result)