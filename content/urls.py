from django.urls import path
import content.views as views

urlpatterns = [
    path("", view=views.home, name="app_home"),
    path("article/<int:id>", view=views.article_page, name="app_article")
]
