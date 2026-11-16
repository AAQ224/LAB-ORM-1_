from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Give your story a captivating title...",
                    "dir": "auto",
                    "autocomplete": "off",
                }
            ),

            "content": forms.Textarea(
                attrs={
                    "placeholder": "Every great story begins with a single thought...\n\nStart writing here.",
                    "dir": "auto",
                    "rows": 12,
                }
            ),
        }