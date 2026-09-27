from bson import ObjectId
from rest_framework.decorators import api_view
from rest_framework.response import Response

from config.mongodb import db


@api_view(["GET", "POST"])
def users_api(request):
    users = db["users"]

    if request.method == "GET":
        data = []

        for user in users.find():
            data.append({
                "id": str(user["_id"]),
                "name": user.get("name"),
                "email": user.get("email"),
                "age": user.get("age"),
            })

        return Response(data)

    if request.method == "POST":
        data = request.data

        result = users.insert_one({
            "name": data.get("name"),
            "email": data.get("email"),
            "age": data.get("age"),
        })

        return Response({
            "message": "User created",
            "id": str(result.inserted_id),
        }, status=201)
        


@api_view(["PUT"])
def update_user(request, user_id):
    users = db["users"]

    result = users.update_one(
        {"_id": ObjectId(user_id)},
        {
            "$set": {
                "name": request.data.get("name"),
                "email": request.data.get("email"),
                "age": request.data.get("age"),
            }
        }
    )

    if result.matched_count == 0:
        return Response(
            {"message": "User not found"},
            status=404
        )

    return Response({
        "message": "User updated"
    })
@api_view(["DELETE"])
def delete_user(request, user_id):
    users = db["users"]

    result = users.delete_one(
        {"_id": ObjectId(user_id)}
    )

    if result.deleted_count == 0:
        return Response(
            {"message": "User not found"},
            status=404
        )

    return Response({
        "message": "User deleted"
    })