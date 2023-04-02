from posixpath import basename
from django.urls import path, include
# from movie.api.views import StreamPlatform_list,  StreamPlatform_details
from movie.api.views import (GetAllStreamPlatformAV, StreamPlatformAV,  StreamPlatformDetailAV, WatchListAV, WatchDetailAV)

urlpatterns = [
    path('liststream/', GetAllStreamPlatformAV.as_view(), name='list-streamplatform'),
    path('stream/', StreamPlatformAV.as_view(), name='streamplatform-list'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),

    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='watch-detail'),
    # path('list/', StreamPlatform_list, name="StreamPlatform_list"),
    # path('<int:pk>', StreamPlatform_details, name="StreamPlatform_details"),
]