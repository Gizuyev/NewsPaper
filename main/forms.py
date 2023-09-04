from django import forms
from .models import Article, Category, Tags, Comments

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'summary', 'content', 'author', 'category', 'image_url', 'tags']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = ['tag_name']

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']



