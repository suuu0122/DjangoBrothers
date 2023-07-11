from django.urls import path

from . import views



app_name = "arsenal_players"
urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<int:player_id>/', views.detail, name="detail"),
]