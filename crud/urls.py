from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from webapi import views

router = routers.DefaultRouter()
router.register(r'passengers', views.PassengerViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
