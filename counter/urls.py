from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.select, name='select'),
    path('select2/<int:id>/', views.post, name='post'),
    path('remove/<int:id>/', views.removes, name='removes'),
    path('update/<int:pk>/', views.ArticleUpdate.as_view(), name='update')
]
