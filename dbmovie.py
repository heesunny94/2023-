from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.nxs4xsn.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})
# 0은 문자열로 진행한다 > [문자열: '']