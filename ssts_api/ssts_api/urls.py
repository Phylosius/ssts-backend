from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from accounts.urls import router as account_router

router = routers.DefaultRouter()
router.registry.extend(account_router.registry)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('dj_rest_auth.urls')),
]
