from django.urls import path
from rest_framework import routers

from faces import views

router = routers.DefaultRouter()
router.register(r'faces', views.FacesViewSet)

urlpatterns = [
    path('register/', views.FacesView.as_view(), name='faces-register'),
    path('modules/get_encodings/', views.FaceEncodingsModule.as_view(), name='faces-module-get-encodings'),
]