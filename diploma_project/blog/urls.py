from django.urls import path
from blog.views import blog_list, BlogDetailView, get_likes

urlpatterns =[
    path('', blog_list, name='blog_list'),
    path('article/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>', get_likes, name='like_post'),
]
