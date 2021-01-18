def get_db():
    from pymongo import MongoClient
    client = MongoClient("mongodb+srv://admin:admin@vertrieb.esobc.mongodb.net/vertrieb?retryWrites=true&w=majority")
    db = client.myFirstMB
    return db

def add_stair(db):
    db.stairs.insert_one({"Treppennummer":"TR2100002"})

def get_stairs(db):
    return db.stairs.find_one()


if __name__ =="__main__":
    db = get_db()
    add_stair(db)
    print (get_stairs(db))