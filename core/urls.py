from django.urls import path
from users import views as user_views
from . import views as core_views

app_name = "core"

urlpatterns = [path("", user_views.LoginView.as_view(), name="loginMain"),
                path("main/", core_views.MainView.as_view(), name="main")]
