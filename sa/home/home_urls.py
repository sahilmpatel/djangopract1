from django.urls import path
from .views import home,profileshow,proshow,hey,showbyorder,loginuser,logoutuser,logoutdone

app_name = "Home"
urlpatterns = [
    path("home/",home,name = "home"),
    path("profile/",profileshow, name = "profileshow"),
    path("loginuser/",loginuser, name = "loginuser"),
    path("logoutuser/", logoutuser, name="logoutuser"),
    path("logoutdone/", logoutdone, name="logoutdone"),
    path("proshow/",proshow, name = "proshow"),
    path("hey/",hey, name = "hey"),
    path("showbyorder/",showbyorder, name = "showbyorder"),

]