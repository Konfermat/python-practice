from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_details, name='post_details'),
]

# http://localhost:8000/главныйurls/urlsприложения
# http://localhost:8000/главныйurls/posts
#