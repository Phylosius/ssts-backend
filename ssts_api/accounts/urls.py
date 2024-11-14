from rest_framework import routers

from accounts import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
