"""StockMonitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from StockMonitor import views


router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'stock', views.StockViewSet)


urlpatterns = [
    # url(r'^login', views.LoginView.as_view()),
    url(r'^logout$', views.LogoutView.as_view()),
    url(r'^login$', views.MyTokenObtainPairView.as_view()),    # 需要添加的内容
    url(r'^user/password$', views.UserPasswrodView.as_view()),
    # url(r'^api/v1/refresh/$', TokenRefreshView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    # url(r'^user',views.UserViewSet.as_view({'get': 'list'}), name="user"),
    url(r'^', include(router.urls)),
]
