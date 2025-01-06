from rest_framework.authtoken import views
from rest_framework import routers
from django.urls import include, path

from .views import PostViewSet, GroupViewSet, CommentList, CommentDetail

app_name = 'api'


router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('posts/<int:post_id>/comments/', CommentList.as_view()),
    path('posts/<int:post_id>/comments/<int:comment_id>/',
         CommentDetail.as_view()),
    path('', include(router.urls)),
]
