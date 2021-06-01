from django.urls import path
from . import views

urlpatterns = [
    path('',views.starting_page,name="starting-page"),
    path("/posts",views.posts,name="posts-page"),
    path("/path/<slug:slug>",views.post_detail,name="post-detail-page"),  #These are standard called slug !
]