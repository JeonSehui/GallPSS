from django.urls import path
from boards import views as board_views

app_name = "boards"

urlpatterns = [path("leftmenu", board_views.LeftMenu.as_view(), name="leftmenu"),
                path("main", board_views.Category.as_view(), name="category"), ]
