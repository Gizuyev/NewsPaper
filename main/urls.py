from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.get_article_by_category, name='get_article_by_category'),
    path('tag/<int:tag_id>/', views.get_article_by_tag, name='get_article_by_tag'),
    path('article/<int:pk>/', views.detail_article, name='detail_article'),
    path('add_article/', views.add_article, name ='add_article'),
    path('add_category/', views.add_category, name ='add_category'),
    path('add_tag/', views.add_tag, name='add_tag'),
    path('article_edit/<int:pk>/', views.EditArticleView.as_view(), name='edit_article'),
    path('add_comment/<int:pk>/', views.add_comment, name='add_comment'),
    path('delete_comment/<int:pk>/', views.delete_comment, name='delete_comment'),
    path('like_article/<int:article_id>/', views.like_article, name='like_article'),
]
