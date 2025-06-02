from datetime import datetime, timezone
from django.shortcuts import render, get_object_or_404
from content.models import Article


def home(request):
    articles = Article.objects.all()
    # articles = Article.objects.filter(is_published=True, publication_date__lte=datetime.now(
    # timezone.utc)).order_by("-publication_date")
    return render(request, "home.jinja", {
        "articles": articles
    })


def article_page(request, id: int):
    article = get_object_or_404(Article, id=id)
    return render(request, "article.jinja", {
        "article": article
    })
