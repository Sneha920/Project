from blog.viewsets import UserViewset
from rest_framework import routers

router = routers.DefaultRouter()
routers = router.register('users',UserViewset)
