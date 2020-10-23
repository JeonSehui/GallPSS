from django.urls import path
from boards import views as board_views

app_name = "boards"

urlpatterns = [path("main", board_views.Category.as_view(), name="main"), ]
