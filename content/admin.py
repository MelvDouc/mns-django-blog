from django.contrib import admin
from content.models import Article


class ArticleAdmin(admin.ModelAdmin):
    # Adds search feature to admin spaces that uses these two fields.
    search_fields = ("title", "content")
    list_filter = ("created_at", "author")
    list_display = ("title", "created_at", "updated_at",
                    "author_name", "content_length")
    ordering = ("title", "-created_at")  # minus sign: desc
    date_hierarchy = "created_at"
    fieldsets = (
        ("Auteur & publication", {
            "fields": ("author", "is_published", "publication_date")
        }),
        ("Contenu", {
            "fields": ("title", "content")
        }),
        ("Médias", {
            "fields": ("image",)
        })
    )

    def author_name(self, article: Article) -> str:
        if article.author is not None:
            return article.author.first_name
        return "[no author]"

    author_name.short_description = "Auteur"

    def content_length(self, article: Article) -> int:
        return len(article.content)

    content_length.short_description = "Longueur"


admin.site.register(Article, ArticleAdmin)
