from django import forms
from content.models import Article


class CommentForm(forms.Form):
    content = forms.CharField(
        label="Votre commentaire",
        widget=forms.Textarea(attrs={
            "rows": 5,
            "cols": 100
        })
    )
