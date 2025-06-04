from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="titre")
    content = models.TextField(verbose_name="contenu")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="date de création"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="date de modification"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="articles",
        null=True,
        blank=True
    )
    is_published = models.BooleanField(default=True, verbose_name="publié")
    publication_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="date de publication"
    )
    image = models.ImageField(
        upload_to="articles",
        null=True,
        blank=True,
        verbose_name="image"
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Comment(models.Model):
    content = models.CharField(max_length=255, verbose_name="commentaire")
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="créé le"
    )
