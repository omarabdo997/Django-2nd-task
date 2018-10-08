from django.urls import path
from . import views
app_name = 'articles'
urlpatterns = [
    path('', views.articlelist, name='list'),
    path('create/', views.article_create, name='create'),
    path('<slug>/', views.article_detail, name='detail'),
]
