from django.urls import path

from apps.articles import views

urlpatterns = [
    path('release_article/', views.ReleaseArticleViews.as_view()),
    path('article/', views.ArticleViews.as_view()),
    path('search/', views.SearchViews.as_view())
]