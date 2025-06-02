from django.urls import path
from content.views import articles_list

urlpatterns = [
    path("", view=articles_list, name="app_articles_list")
]
