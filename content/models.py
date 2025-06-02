from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="titre")
    content = models.TextField(verbose_name="Contenu")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Date de modification")
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="articles", null=True, blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Publié")
    publication_date = models.DateTimeField(
        null=True, blank=True, verbose_name="Date de publication")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
