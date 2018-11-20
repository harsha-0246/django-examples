from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """
    PostForm:   Name of the form mentioning this as a django's ModelForm
    class Meta: whcih model is to be used to create
    """
    class Meta:
        """
        title and text fileds to be taken from web page and user will be
        current user and created date: today
        """
        model = Post
        fields = ('title', 'text',)