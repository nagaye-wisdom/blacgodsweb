from django.urls import path
from . views import VideoListView, VideoDetailView, PictureListView, PictureDetailView
from . import views

urlpatterns = [
    path('gallery/', VideoListView.as_view(), name='videos'),
    path("video_search", views.video_search, name="video_search"),
    path("picture_search", views.picture_search, name="picture_search"),
    path('gallery/<int:pk>/', VideoDetailView.as_view(), name='video'),
    path('pic_detail/<int:pk>/', PictureDetailView.as_view(), name='pic_detail'),
    path('pictures/', PictureListView.as_view(), name='pictures'),
]

