import pymongo
client= pymongo.MongoClient('mongodb://admin:admin@ds021182.mlab.com:21182/c4e')
db= client['c4e']
db.posts.insert_one({'title':'Chuyện code','author':'Nguyễn Thị Liên','content':'Hiện trạng: Có biết cái vẹo gì đâu,chả có gì đặc biệt cả '})