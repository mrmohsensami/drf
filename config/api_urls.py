from rest_framework import routers
from post.api_views import PostViewset

router = routers.SimpleRouter()
router.register('posts', PostViewset, basename='post')