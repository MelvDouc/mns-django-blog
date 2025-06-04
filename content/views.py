from django.contrib import messages
from django.http import HttpRequest, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404

from content.models import Article, Comment
from content.forms import CommentForm


def home(request: HttpRequest):
    articles = Article.objects.all()
    # articles = Article.objects.filter(is_published=True, publication_date__lte=datetime.now(
    # timezone.utc)).order_by("-publication_date")
    return render(request, "home.jinja", {
        "articles": articles
    })


def article_page(request: HttpRequest, id: int):
    article = get_object_or_404(Article, id=id)

    match request.method:
        case "GET":
            comments = article.comments.all().order_by("-created_at")  # type: ignore
            return render(request, "article.jinja", {
                "article": article,
                "form": CommentForm(),
                "comments": comments
            })
        case "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = Comment(
                    article=article,
                    content=form.cleaned_data["content"]
                )
                comment.save()
            messages.success(request, "The comment was added successfully.")
            return redirect("app_article", id=id)
        case _:
            return HttpResponseNotAllowed(["GET", "POST"])
