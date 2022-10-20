from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import PostListView, GroupListView, CommentListView, FollowListView

router_v1 = DefaultRouter()
router_v1.register('posts', PostListView)
router_v1.register('groups', GroupListView)
router_v1.register('follow', FollowListView, basename='followers')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentListView, basename='comments')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
