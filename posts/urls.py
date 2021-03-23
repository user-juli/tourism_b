from django.urls import path
from posts import views

urlpatterns = [
    path(route='myblog',view=views.PostsFeedView.as_view(),name='myblog'),
    path(route='posts/<slug:url>/',view=views.PostDetailView.as_view(),name='detail'),
    path(route='posts/save_comment',view=views.save_comment,name='save_comment'),
]
