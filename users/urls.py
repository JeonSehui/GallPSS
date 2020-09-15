from django.urls import path
from . import views as user_view

app_name = "users"

urlpatterns = [path("login", user_view.loginProc, name="loginProc"),
path("logout", user_view.log_out, name="logout"),]