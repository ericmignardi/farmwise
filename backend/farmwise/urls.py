from django.urls import path
from . import views

urlpatterns = [
    path("farms/", views.farm_list, name="farm-list"),
    path("farms/<int:pk>/", views.farm_detail, name="farm-detail"),
    path("crops/", views.crop_list, name="crop-list"),
    path("assets/", views.asset_list, name="asset-list"),
    path("wealth/", views.wealth_list, name="wealth-list"),
    path("chat/", views.chat, name="chat"),
]
