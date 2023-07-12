from django.urls import path

from . import views



app_name = "app"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:memo_id>', views.detail, name="detail"),
    path('new_memo', views.new_memo, name="new_memo"),
]