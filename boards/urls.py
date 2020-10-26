from django.urls import path
from boards import views as board_views

app_name = "boards"

urlpatterns = [path("main", board_views.Category.as_view(), name="main"),
                path("boardid/<int:id>", board_views.GetBoardItem.as_view(), name="getItemDetail"),
                path("itemid/<int:id>", board_views.GetBoardItem.as_view(), name="getItemDetail"),
                path("create/<int:id>", board_views.GetBoardItem.as_view(), name="getItemDetail")]
