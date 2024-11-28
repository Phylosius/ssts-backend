from rest_framework import routers

from faces import views

router = routers.DefaultRouter()
router.register(r'faces', views.FacesViewSet)
