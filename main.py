from flask import Flask, Response, request
import pymongo
import json
from bson.objectid import ObjectId
app = Flask (__name__)

try:
    mongo = pymongo.MongoClient(
        host='mongodb+srv://admin:admin@vertrieb.esobc.mongodb.net/vertrieb?retryWrites=true&w=majority',
        serverSelectionTimeoutMS = 1500
    )

    db = mongo.stairs_2021
    mongo.server_info()
except:
    print("ERROR MongeDB")

###########################DELETE##########################################

@app.route("/user/<id>", methods =["DELETE"])
def delete_stair(id):

    try:
        dbResponse =db.user.delete_one({"_id":ObjectId(id)})

        if dbResponse.delete_count ==1:

            return Response(
                response=json.dumps({"message": "stair delete", "id": f"{id}"}),
                status=200,
                mimetype="application/json"
            )
        else:
            return Response(
                response=json.dumps({"message": "stair delete", "id": f"{id}"}),
                status=200,
                mimetype="application/json"
            )


    except Exception as ex:
        print("###########################")
        print(ex)
        print("###########################")
        return Response(
            response= json.dumps({"message":"can not delete stair"}),
            status = 500,
            mimetype="application/json"
        )

###########################UPDATE##########################################

@app.route("/user/<id>", methods =['PATCH'])
def update_stair(id):
    try:
        dbResponse = db.user.update_one(
            {"_id": ObjectId(id)},
            {"$set":{"Bauvorhaben":request.form["Bauvorhaben"]}}
        )
        #for attr in dir(Response):
        #    print(f"#########{attr}########")

        if dbResponse.modfied_count == 1:
            return Response(
                response=json.dumps({"message": "stair updated"}),
                status=200,
                mimetype="application/json"
            )
        else:
            return Response(
                response=json.dumps({"message": "nothing to update"}),
                status=200,
                mimetype="application/json"
            )
    except Exception as ex:
        print("###########################")
        print(ex)
        print("###########################")
        return Response(
            response= json.dumps({"message":"can not update stair"}),
            status = 500,
            mimetype="application/json"
        )


###########################READ##########################################
@app.route("/user", methods =['GET'])
def get_some_stair():
    try:
        data = list(db.user.find({"Bauvorhaben":"Brees"}))
        print (data)
        for stair in data:
            stair["_id"]=str(stair["_id"])
        return Response(
            response= json.dumps(data),
            status = 500,
            mimetype="application/json"
        )

    except Exception as ex:
        print(ex)
        return Response(
            response= json.dumps({"message":"can not read stair"}),
            status = 500,
            mimetype="application/json"
        )


##########################CREATE###########################################
@app.route('/user', methods =['POST'])
def create_user():
    try:
        stair = {
            "Treppennummer":request.form["Treppennummer"],
            "Bauvorhaben": request.form ["Bauvorhaben"]}
        dbResponse = db.user.insert_one(stair)
        print(dbResponse.inserted_id)
       # for attr in dir(dbResponse):
        #    print(attr)
        return Response(
            response= json.dumps(
            {"message":"stair created",
                      "id":f"{dbResponse.inserted_id}"
             }
            ),
            status = 200,
            mimetype="application/json"
        )

    except Exception as ex:
        print('##################')
        print(ex)

if __name__ == '__main__':
    app.run(port=42, debug=True)