from django.urls import path
from .views import users_api, update_user, delete_user

urlpatterns = [
    path("users/", users_api),
    path("users/<str:user_id>/", update_user),
    path("users/<str:user_id>/delete/", delete_user),
]