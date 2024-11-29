from django.forms import ModelForm
from django import forms
from .models import ChocoPost, Comment

class ChocoPostForm(ModelForm):
    class Meta:
        model = ChocoPost
        fields = ['category', 'title', 'comment', 'comment2', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

