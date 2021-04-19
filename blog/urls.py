from django.urls import path
from blog.views import get_profile, get_my_page, PostView

urlpatterns = [
    path('hello/', get_profile),
    path('my_page/', get_my_page),
    path('posts/', PostView.as_view()),
]
