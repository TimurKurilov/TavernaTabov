from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path
from django.urls import include
from catalog.views import ElectroGuitarViewsets

router = DefaultRouter()
router.register(r'electro', ElectroGuitarViewsets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
