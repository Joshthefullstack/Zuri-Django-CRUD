from curses import meta
from django import forms
from .models import Post

class Post_forms(forms):
    class meta:
        model = Post
        fields = [
            "title",
            "slug",
            "author",
            "body",
            "published",
            "created",
            "updated",
            "status"
        ]
