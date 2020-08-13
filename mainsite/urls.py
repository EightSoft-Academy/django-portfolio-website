from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('post/<str:pk>/', views.post, name='post'),
    path('profile/', views.profile, name='profile'),

    # CRUD PATHS
    path('create_post/', views.create_post, name='create_post'),
    path('update_post/<str:pk>/', views.update_post, name='update_post'),
    path('delete_post/<str:pk>/', views.delete_post, name='delete_post'),
]
