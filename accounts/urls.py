from django.urls import path
from . import views

urlpatterns = [
    path("auth/sign-up", views.register, name="app_register"),
    path("auth/log-in", view=views.login, name="app_login"),
    path("auth/log-out", view=views.logout, name="app_logout"),
    path("profile", view=views.profile, name="app_profile")
]
