from .views import (
        ArticleListView,
        ArticleUpdateView,
        ArticleDetailView,
        ArticleDeleteView,
        ArticleCreateView,
    )
from django.urls import path


urlpatterns = [
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('', ArticleListView.as_view(), name='article_list'),
]
