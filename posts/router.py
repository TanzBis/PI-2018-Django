from rest_framework import routers

from posts.views import postsViewSet, postStatusViewSet

router = routers.DefaultRouter()
router.register(r'post', postsViewSet)
router.register(r'post/status', postStatusViewSet)