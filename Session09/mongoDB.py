import pymongo
from bson.objectid import ObjectId
client = pymongo.MongoClient(
    "mongodb+srv://admin:12345678Abc@demo-cluster-mvmw2.mongodb.net/test?retryWrites=true&w=majority")

db = client.restaurant


def update_food_by_id(food_id, name, price):
    db.foods.update_one({'_id': ObjectId(food_id)},
                        {'$set': {'name': name, 'price': price}})


def find_food_by_id(food_id):
    return db.foods.find_one({'_id': ObjectId(food_id)})


def get_all_food():
    return list(db.foods.find())


def insert_food(name, price):
    db.foods.insert_one({'name': name, 'price': price})


def delete_food_by_id(food_id):
    db.foods.delete_one({'_id': ObjectId(food_id)})

# db.foods.insert_one({'name': 'ga ran', 'price': 160})
# db.foods.insert_one({'name': 'com rang', 'price': 30})
