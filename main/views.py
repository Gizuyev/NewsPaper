from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ArticleForm, CategoryForm, TagForm, CommentsForm
from .models import Article, Category, Comments, Likes

def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    context = {
        'article_list': articles,
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def get_article_by_category(request, category_id):
    articles = Article.objects.filter(category__id=category_id)
    categories = Category.objects.all()
    context = {
        'article_list': articles,
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def get_article_by_tag(request, tag_id):
    articles = Article.objects.filter(tags__id=tag_id)
    categories = Category.objects.all()
    context = {
        'article_list': articles,
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def detail_article(request, pk):
    article = get_object_or_404(Article, id=pk)
    form = CommentsForm()

    article.increment_view_count()

    context = {
        'article': article,
        'form': form
    }
    return render(request, 'main/detail_article.html', context)

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }        
    return render(request, 'main/add_article.html', context)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'main/add_category.html', context)

def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TagForm()
    context = {
        'form': form
    }
    return render(request, 'main/add_tag.html', context)


class EditArticleView(UpdateView):
    model = Article
    template_name = 'main/edit_article.html'
    form_class = ArticleForm

def add_comment(request, pk):
    article = get_object_or_404(Article, id=pk)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user.author
            comment.save()
            return redirect('detail_article', pk=article.id)
        

def delete_comment(request, pk):
    comment = get_object_or_404(Comments, pk=pk)

    if request.user.author == comment.user:
        comment.delete()

    return redirect('detail_article', pk=comment.article.id)


def like_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    user_has_liked = Likes.objects.filter(who_likes=request.user, article=article).exists()
    existing_like = Likes.objects.filter(who_likes=request.user, article=article).first()

    if user_has_liked:
        existing_like.delete()
    else:
        new_like = Likes(who_likes=request.user, article=article, count_of_likes=1)
        new_like.save()

    return HttpResponseRedirect(reverse('detail_article', args=[article_id]))
