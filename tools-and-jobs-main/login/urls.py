from django.urls import path
from .views import login_view,index_view,logout_view


urlpatterns = [
    # path("signup/", signup_view, name="signup"),
    path("", login_view, name="login"),
    path("dashboard/", index_view, name="index"),
    path("logout/", logout_view, name="logout"),

]